Supplai REST API Client
=======================

OVERVIEW
--------

`Supplai Client <https://bitbucket.org/supplai/supplai-client>`_ is a python3 wrapper for Supplai's REST API v1.
This library currently implements the features released under `version 0.100.1 <https://api.supplai.com.br/doc/release-notes/>`_ of Supplai's REST API.

Requirements
------------

This project requires:

    * Python 3.4 or earlier
    * git client
    * virtualenvwrapper/virtualenv for local development


Installation
------------

.. code-block:: bash

    $ pip install git@bitbucket.org:supplai/supplai-client.git

Or, you can download the source and

.. code-block:: bash

    $ git clone git@bitbucket.org:supplai/supplai-client.git

    $ cd supplai_client
    $ python setup.py install

USAGE
-----

1. Create a user on `<https://www.supplai.com.br>`_ to get a API Access Token.
2. Import the supplai_client module and create an instance with your access token:

.. code-block:: python

    >> from supplai_client import API
    >> from supplai_client.exceptions import SupplaiError
    >>
    >> access_token = "<Supplai Access token>"
    >> client = API(environment="practice", access_token=access_token)

    >> try:
    >>     result = client.user.get_users()
    >> # In case of http status 400
    >> except SupplaiError as exc:
    >>     print(str(exc))
    >>
    >> # Use the result as object
    >> print(result.as_obj())
    UserUsers(
        previous=None,
        count=1,
        next=None,
        results=[
            NamelessModel(occupation=None, full_name='Admin System',
                image=None, cpf='', is_superuser=True, cellphone='', email='', sex=None, username='admin', birthdate='09/09/1999',
                logged_as='', id=1, is_temp=False, is_active=True)
        ]
    )
    >>
    >> # Use the result as dict
    >> print(result.as_dict())
    {'count': 1,
     'next': None,
     'previous': None,
     'results': [{'id': 1,
       'username': 'admin',
       'full_name': 'Admin System',
       'sex': None,
       'birthdate': '09/09/1999',
       'cpf': '',
       'cellphone': '',
       'email': '',
       'image': None,
       'occupation': None,
       'logged_as': '',
       'is_superuser': True,
       'is_active': True,
       'is_temp': False}
      ]
     }




Contributing
------------

Please send pull requests, very much appreciated.


1. Fork the `repository <https://bitbucket.org/supplai/supplai-client>`_ on GitHub.
2. Create a virtualenv.
3. Install requirements. ``pip install -r requirements-dev.txt``
4. Install pre-commit. ``pre-commit install``
5. Make a branch off of master and commit your changes to it.
6. Create a Pull Request with your contribution


NOTES
-----

* Supplai API REST Client is still under development, some functionality have not yet been implemented, but I will keep an eye on it, and as soon as it gets implemented I will update this library accordingly.


.. |Travis Build Status| image:: https://travis-ci.org/rhenter/supplai_client.svg?branch=master
   :target: https://travis-ci.org/rhenter/supplai_client.svg?branch=master
.. |Coverage Status| image:: https://coveralls.io/repos/github/rhenter/supplai_client/badge.svg?branch=master
   :target: https://coveralls.io/github/rhenter/supplai_client?branch=master
.. |Code Health| image:: https://landscape.io/github/rhenter/supplai_client/master/landscape.svg?style=flat
   :target: https://landscape.io/github/rhenter/supplai_client/master
.. |PyPI Version| image:: https://img.shields.io/pypi/pyversions/supplai_client.svg?maxAge=2000000
   :target: https://pypi.python.org/pypi/supplai_client
.. |PyPI License| image:: https://img.shields.io/pypi/l/supplai_client.svg?maxAge=360
   :target: https://bitbucket.org/supplai/supplai-client/blob/master/LICENCE
.. |PyPI latest| image:: https://img.shields.io/pypi/v/supplai_client.svg?maxAge=180
   :target: https://pypi.python.org/pypi/supplai_client
