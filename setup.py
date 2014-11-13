from setuptools import setup

setup(
    name='pyqode-uic',
    version='0.1.1',
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
    },
     classifiers=[
        'Environment :: X11 Applications :: Qt',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
