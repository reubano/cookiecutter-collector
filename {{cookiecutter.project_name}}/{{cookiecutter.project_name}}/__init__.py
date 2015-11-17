# -*- coding: utf-8 -*-
# vim: sw=4:ts=4:expandtab

"""
{{ cookiecutter.project_name }}
{{ '~' * cookiecutter.project_name|count }}

{{ cookiecutter.project_description }}

Examples:
    literal blocks::

        python example_google.py

Attributes:
    CONSTANT (str): Module level constant
"""

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals)

from manager import Manager

manager = Manager()

__title__ = '{{ cookiecutter.project_name }}'
__author__ = '{{ cookiecutter.author_name }}'
__description__ = '{{ cookiecutter.project_description }}'
__email__ = '{{ cookiecutter.author_email }}'
__version__ = '{{ cookiecutter.version }}'
__license__ = '{{ cookiecutter.license }}'
__copyright__ = 'Copyright {{ cookiecutter.year }} {{ cookiecutter.author_name }}'

CONSTANT = 'constant'


class {{ cookiecutter.project_name | capitalize }}(object):
    """This is a description of the class.

    Attributes:
        argument (str): Description of `argument`.
        kwarg (Optional[str]): Description of `kwarg`.
    """

    def __init__(self, argument, kwarg=None):
        """Initialization method.

        Args:
            argument (int): The first parameter.
            kwarg (Optional[str]): The second parameter (default: None).

        Returns:
            New instance of :class:`{{ cookiecutter.project_name | capitalize }}`

        Examples:
            >>> {{ cookiecutter.project_name | capitalize }}()  #doctest: +ELLIPSIS
            <{{ cookiecutter.project_name }}.{{ cookiecutter.project_name | capitalize }} object at 0x...>
        """

        self.argument = argument
        self.kwarg = kwarg

    @property
    def property(self):
        """Show upper cased argument.

        Returns:
            str: upper cased argument

        Examples:
            >>> {{ cookiecutter.project_name | capitalize }}('hello').property
            u'HELLO'
        """
        return self.argument.upper()

    def multiply(self, value):
        """Double argument.

        Args:
            value (int): number to multiply by.

        Returns:
            str: argument multiplied by value

        Examples:
            >>> {{ cookiecutter.project_name | capitalize }}('piki').multiply(2)
            u'pikipiki'
        """
        return self.argument * value


@manager.command
def ver():
    """Show {{ cookiecutter.project_name }} version"""
    print('v%s' % __version__)


if __name__ == '__main__':
    manager.main()
