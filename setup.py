from distutils.core import setup

setup(
    name='pyqode-uic',
    version='1.0',
    py_modules=['pyqode_uic', 'pyqode_rcc'],
    url='https://github.com/pyQode/pyqode-pyuic',
    license='MIT',
    author='Colin Duquesnoy',
    author_email='colin.duquesnoy',
    description='pyQode Qt ui compiler',
    entry_points={
        'console_scripts': [
            'pyqode-uic = pyqode_uic:main_uic',
            'pyqode-rcc = pyqode_uic:main_rcc',
        ],
    }
)
