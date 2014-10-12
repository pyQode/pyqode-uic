.. image:: https://raw.githubusercontent.com/pyQode/pyqode.core/master/doc/source/_static/pyqode-banner.png


About
-----

.. image:: http://img.shields.io/pypi/v/pyqode-uic.png
   :target: https://pypi.python.org/pypi/pyqode-uic/
   :alt: Latest PyPI version

.. image:: http://img.shields.io/pypi/dm/pyqode-uic.png
   :target: https://pypi.python.org/pypi/pyqode-uic/
   :alt: Number of PyPI downloads

Compile Qt Designer ui files to python scripts using the ``pyqode.qt``
package instead of ``PyQt5``.

The tool is a simple wrapper on top of ``pyuic5``/``pyrcc5``. It does two thing:
    - run pyuic5 or pyrcc5 (with the supplied arguments)
    - replace ``from PyQt5 import`` by ``from pyqode.core.qt import`` in the

This tool is part of the `pyQode`_ project.

- `Issue tracker`_
- `Wiki`_
- `Contributing`_
- `Changelog`_


Usage
-----

Just run ``pyqode-uic`` or ``pyqode-rcc`` with the same arguments as you would have
used if you were using ``pyuic5`` or ``pyrcc5``.

For example::

    pyqode-uic --from-imports my_file.ui -o my_file_ui.py
    pyqode-rcc my_resources.qrc -o my_resources_rc.py



Installation
------------
::

    pip3 install pyqode-uic

License
-------

This project is licensed under the **MIT license**.

.. _Changelog: https://github.com/pyQode/pyqode-uic/blob/master/CHANGELOG.rst
.. _Contributing: https://github.com/pyQode/pyqode-uic/blob/master/CONTRIBUTING.rst
.. _pyQode: https://github.com/pyQode/pyQode
.. _Issue tracker: https://github.com/pyQode/pyQode/issues
.. _Wiki: https://github.com/pyQode/pyQode/wiki
