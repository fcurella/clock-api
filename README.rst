Clock
=====

An over-engineered Alarm Clock with API.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT

.. image:: https://github.com/fcurella/clock-api/raw/master/docs/assets/screenshots/owl.png

Concept
-------

The main idea is to provide a very flexible backend and a frontend that can be custom designed.
I've included two designs: an owl and an analog clock. But feel free to fork and make your own!

I usually keep the clock open on a tiny browser window on my second monitor to keep me company.

Alarms
------

Alarms can have arbitrary attributes attached (eg: a color, or the URL of a picture), and
frontends may interpret them.

Right now alarms are specified using crontabs, but I plan to add support for other schedulers
in the future. For example, you could use a solar schedule to create an alarm that fires at dawn.

Creating Alarms
^^^^^^^^^^^^^^^

You can add alarms by using the admin (at ``/admin/``) or by using the API at ``/api/alarms/``

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser


Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest


Celery
^^^^^^

This app comes with Celery.

To run celery beat:

.. code-block:: bash

    cd clock
    celery -A config.celery_app beat -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.


Deployment
----------

You can deploy locally by using `Garden.io <https://garden.io/>`_:

.. code-block:: bash

    garden run task migrate
    garden run task build
    garden deploy

You can then visit http://clock.local.app.garden.

Or you can deploy straight to heroku:

.. image:: https://www.herokucdn.com/deploy/button.svg
   :alt: Deploy
   :target: https://heroku.com/deploy
