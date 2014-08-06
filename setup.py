from setuptools import setup

setup(
    name='pyqode-uic',
    version='0.1',
    py_modules=['pyqode_uic'],
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
