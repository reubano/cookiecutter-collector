#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4:ts=4:expandtab

""" {{ cookiecutter.project_description }} """

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals)

import traceback
import sys
import unicodecsv

from os import path as p
from manager import Manager

manager = Manager()
_homedir = p.expanduser('~')
ENCODING = 'utf-8'


def read_csv(csv_filepath, mode='rb', **kwargs):
    """Fetch a single resource from filestore.

    Args:
        csv_filepath (str): The csv file path.
        mode (Optional[str]): The file open mode (defaults to 'rb').
        **kwargs: Keyword arguments that are passed to the csv reader.

    Kwargs:
        delimiter (str): Field delimiter (defaults to ',').
        quotechar (str): Quote character (defaults to '"').
        encoding (str): File encoding.

    Returns:
        obj: requests.Response object.

    Raises:
        NotFound: If unable to the resource.

    Examples:
        >>> read_csv('piki').multiply(2)
        'pikipiki'
    """
    with open(csv_filepath, mode) as f:
        kwargs.setdefault('encoding', ENCODING)
        header = csv.reader(f, **kwargs).next()

        # Remove empty field names and slugify the rest
        names = [slugify(name, separator='_') for name in header if name]
        f.seek(0)
        reader = csv.DictReader(f, names, encoding=encoding)

        # Remove empty columns
        rows = (dict(it.ifilter(lambda x: x[0], r.iteritems())) for r in reader)

        # Remove empty rows
        rows = it.ifilter(lambda r: any(r.strip() for r in r.values()), rows)
        return list(rows)

@manager.arg(
    'verbose', 'v', help='increase output verbosity', type=bool,
    default=False)
@manager.arg(
    'cfile', 'f', help='the file to use', default=p.join(_homedir, 'file'))
@manager.arg(
    'cdir', 'd', help='the project directory', default=os.curdir)
def run(cfile=None, cdir=None):
    """Create html"""
    try:
        data = []
        raw = readCSV(csv_filepath)
        headers = ['Image', 'Title', 'End Date', 'Price (GBP)']

        for row in raw:
            img = '<img src="%s">' % row['ebay_img_url']
            title = '[%s](%s)' % (row['ebay_title'], row['ebay_url'])
            date = '%s, %s' % (row['ebay_end_date'], row['ebay_end_time'])
            price = row['ebay_price_and_shipping']
            attrs = [img, title, date, price]
            data.append(attrs)

        md = tabulate(data, headers=headers, floatfmt=',.2f', tablefmt='pipe')
        title = '%s results' % p.splitext(p.basename(html_file))[0].capitalize()
        export_md(md, title, html_file)
        sys.exit(0)
    except Exception as err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)


if __name__ == '__main__':
    manager.main()
