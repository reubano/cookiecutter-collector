======================
cookiecutter-collector
======================

A Python data collector Cookiecutter_ template. The scraper is designed to
work in a ScraperWiki_ "box", however it can be deployed virtually in any Unix
environment. For detailed documentation about how to create and manage scrapers
on ScraperWiki please refer to its `official documentation`_.

Usage
-----

Generate a new collector::

    cookiecutter https://github.com/reubano/cookiecutter-collector.git

Then:

* Edit `config.py`_.
* Edit `app/utils.py`_.
* Edit `app/models.py`_.
* Run `manage setup` to create the db.
* Run `manage run` to populate the db.

Collector Structure
-------------------

The default way to use ScrapeWiki is to store data in a SQLite database named
`scraperwiki.sqlite` in the user's root directory. This enables a series of
features such as an interactive SQL querier, an html table view with filters,
API endpoints for making remote SQL queries, etc.

The folder structure is as follows::

    collector-skeleton
        +---LICENSE
        +---Makefile
        +---README.md
        +---app
        |   +---__init__.py
        |   +---models.py
        |   +---utils.py
        +---bin
        |   +---check-stage
        |   +---upload
        |   +---setup
        +---config.py
        +---dev-requirements.txt
        +---http
        |   +---index.html
        +---manage.py
        +---requirements.txt
        +---setup.cfg
        +---setup.py
        +---tests
            +---__init__.py
            +---standard.rc
            +---test.sh

* :code:`manage.py` contains the main script commands.
* :code:`config.py` contains the configuration settings.
* :code:`http` generally contains an `index.html` file with the summary of the scraping task and any other files that are intended to be available through an API endpoint, such as a `log.txt` file.
* :code:`app` contains the collector model and initialization.

Looking for collector examples?
-------------------------------

* `reubano/hdxscraper-acled`_: Armed Conflict Location & Event Data Project (ACLED) Realtime Data collector.
* `reubano/hdxscraper-fao`_: Food Aid Organization Data collector.
* `reubano/hdxscraper-fts`_: UN Financial Tracking Service (FTS) API collector.

Want to contribute?
-------------------

I will glady accept pull requests if they improve the collector development experience.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _ScraperWiki: http://scraperwiki.com/
.. _`official documentation`: https://scraperwiki.com/help
.. _`config.py`: {{cookiecutter.project_name}}/config.py
.. _`app/utils.py`: {{cookiecutter.project_name}}/app/utils.py
.. _`app/models.py`: {{cookiecutter.project_name}}/app/models.py
.. _Travis-CI: http://travis-ci.org/
.. _`reubano/hdxscraper-acled`: https://github.com/reubano/hdxscraper-acled
.. _`reubano/hdxscraper-fao`: https://github.com/reubano/hdxscraper-fao
.. _`reubano/hdxscraper-fts`: https://github.com/reubano/hdxscraper-fts
