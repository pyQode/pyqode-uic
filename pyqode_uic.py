"""
Compile Qt ui files to python scripts using the ``pyqode.qt``
package instead of ``PyQt5``.

The tool is a simple wrapper on top of ``pyuic5``.

It does two thing:
    - run pyuic5 (with the supplied arguments)
    - replace ``from PyQt5 import`` by ``from pyqode.qt import`` in the

"""
import re
import sys
import os


def fix_imports(script):
    """
    Replace "from PyQt5 import" by "from pyqode.qt import".

    :param script: script path
    """
    with open(script, 'r') as f_script:
        lines = f_script.read().splitlines()
    new_lines = []
    for l in lines:
        if l.startswith("import "):
            l = "from . " + l
        if "from PyQt5 import" in l:
            l = l.replace("from PyQt5 import", "from pyqode.qt import")
        new_lines.append(l)
    with open(script, 'w') as f_script:
        f_script.write("\n".join(new_lines))


def main(tool):
    global args, cmd, p, match, output
    args = ' '.join(sys.argv[1:])
    cmd = '%s %s' % (tool, args)
    p = re.compile(r'-o .*\.py')
    match = re.search(p, args)
    status = os.system(cmd)
    if status == 0:
        if match:
            output = match.group().replace('-o', '').strip()
            fix_imports(output)
        else:
            print('Error: no output specified', file=sys.stderr)
    else:
        return status


def main_uic():
    return main('pyuic5')


def main_rcc():
    return main('pyrcc5')
