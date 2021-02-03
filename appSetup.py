from setuptools import setup

APP = ['menubar.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'art/icon1.png',
    'plist': {
        'CFBundleShortVersionString': '0.2.0',
        'LSUIElement': True,
    },
    'packages': ['rumps', 'os'],
}

setup(
    app=APP,
    name='Presentation Mode',
    py_modules=['presentationMode'],
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], 
    install_requires=['rumps']
)