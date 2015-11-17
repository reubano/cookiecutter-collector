#!/usr/bin/env python
from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals)

import os.path as p
import swutils
import config

from subprocess import call

from flask import current_app as app
from flask.ext.script import Manager
from tabutils.process import merge

from app import create_app, db, utils, __title__, models


manager = Manager(create_app)
manager.add_option('-m', '--mode', default='Development')
manager.main = manager.run

_basedir = p.dirname(__file__)


@manager.command
def check():
    """Check staged changes for lint errors"""
    call(p.join(_basedir, 'bin', 'check-stage'), shell=True)


@manager.command
def lint():
    """Check style with flake8"""
    call('flake8')


@manager.command
def pipme():
    """Install requirements.txt"""
    call('sudo pip install -r requirements.txt', shell=True)


@manager.command
def require():
    """Create requirements.txt"""
    cmd = 'pip freeze -l | grep -vxFf dev-requirements.txt > requirements.txt'
    call(cmd, shell=True)


@manager.command
def test():
    """Run nose and script tests"""
    call('nosetests -xv', shell=True)


@manager.command
def createdb():
    """Creates database if it doesn't already exist"""
    with app.app_context():
        db.create_all()
        print('Database created')


@manager.command
def cleardb():
    """Removes all content from database"""
    with app.app_context():
        db.drop_all()
        print('Database cleared')


@manager.command
def setup():
    """Removes all content from database and creates new tables"""
    with app.app_context():
        cleardb()
        createdb()


def populate():
    """Populates db with most recent data"""
    with app.app_context():
        extra = {'mixin': models.BaseMixin, 'get_name': lambda x: 'ym%s' % x}
        kwargs = merge([app.config, extra])
        swutils.populate(utils.gen_data, db.engine, **kwargs)
        # swutils.populate(utils.gen_data, db.engine, models, **app.config)


@manager.command
def run():
    """Populates all tables in db with most recent data"""
    with app.app_context():
        args = (config.RECIPIENT, app.config.get('LOGFILE'), __title__)
        exception_handler = swutils.ExceptionHandler(*args).handler
        swutils.run_or_schedule(populate, app.config['SW'], exception_handler)


@manager.option(
    '-s', '--stag', help='migrate to staging site', action='store_true')
def migrate(stag=False):
    """Run nose tests"""
    call([p.join(_basedir, 'bin', 'migrate'), 'stag' if stag else 'prod'])

if __name__ == '__main__':
    manager.run()
