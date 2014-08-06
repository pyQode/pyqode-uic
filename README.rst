pyqode-uic
==========

Compile Qt ui files to python scripts using the ``pyqode.core.qt`` package
instead of ``PyQt5``.

The tool is a simple wrapper on top of ``pyuic5``. It does two thing:
    - run pyuic5 (with the supplied arguments)
    - replace ``from PyQt5 import`` by ``from pyqode.core.qt import`` in the

Usage
-----

Just run pyqode-pyuic with the same arguments as you would have used if you
were using ``pyuic5``.

For example::

    pyqode-uic --from-imports my_file.ui -o my_file_ui.py

or::

    python3 pyqode_uic.py --from-imports my_file.ui -o my_file_ui.py

Installation
------------
::

    pip3 install pyqode-uic

License
-------

This project is licensed under the MIT license.
