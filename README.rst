Cookiecutter Houdini Project
****************************

.. image:: https://readthedocs.org/projects/cookiecutter-houdini-project/badge/?version=latest
    :target: https://cookiecutter-houdini-project.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Cookiecutter_ template for a Houdini Python project.

* GitHub repo: https://github.com/Jawabiscuit/cookiecutter-houdini-project.git
* Documentation: https://cookiecutter-houdini-project.readthedocs.io/en/latest/
* Free software: BSD license

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``pytest``
* Sphinx_ docs: Documentation ready for generation with, for example, `Read the Docs`_

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher, latest version tested being 1.7.2)::

    pip install -U cookiecutter

Generate a Houdini Python project::

    cookiecutter https://github.com/Jawabiscuit/cookiecutter-houdini-project.git

Then:

* Create a repo and put it there.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Release your package by pushing a new tag to master.
* Add a ``requirements.txt`` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files

For more details, see the `cookiecutter-houdini-project tutorial`_.

.. _`cookiecutter-houdini-project tutorial`: https://cookiecutter-houdini-project.readthedocs.io/en/latest/tutorial.html

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `audreyfeldroy/cookiecutter-pypackage`_: The Python cookiecutter package this package was derived from.

* Also see the `network`_ and `family tree`_ for this repo. (If you find
  anything that should be listed here, please add it and send a pull request!)

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _Sphinx: http://sphinx-doc.org/
.. _Read the Docs: https://readthedocs.io/

.. _`audreyfeldroy/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _github comparison view: https://github.com/audreyr/cookiecutter-pypackage/compare/Jawabiscuit:master...master
.. _`network`: https://github.com/Jawabiscuit/cookiecutter-houdini-project/network
.. _`family tree`: https://github.com/Jawabiscuit/cookiecutter-houdini-project/network/members
