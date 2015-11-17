# -*- coding: utf-8 -*-
"""
    app
    ~~~

    Provides the flask application
"""
from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals)

import config

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

__version__ = '0.5.0'

__title__ = '{{ cookiecutter.project_name }}'
__author__ = '{{ cookiecutter.author_name }}'
__description__ = ('{{ cookiecutter.project_description }}')

__email__ = '{{ cookiecutter.author_email }}'
__license__ = '{{ cookiecutter.license }}'
__copyright__ = 'Copyright 2015 {{ cookiecutter.author_name }}'

db = SQLAlchemy()


def create_app(mode=None):
    app = Flask(__name__)
    db.init_app(app)

    if mode:
        app.config.from_object(getattr(config, mode))
    else:
        app.config.from_envvar('APP_SETTINGS', silent=True)

    return app
