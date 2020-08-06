from setuptools import setup

APP = ['frontend.py']
DATA_FILES = ['backend.py', 'books.db']
OPTIONS = {
 'argv_emulation': True,
 'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)