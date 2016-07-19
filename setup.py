from setuptools import setup

APP = ['pokegostatus.py']
DATA_FILES = ['icons']
OPTIONS = {
    'iconfile':'icons/appicon.icns',
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps', 'bs4', 'requests'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
