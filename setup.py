from setuptools import setup

APP = ['openai_chat_app.py']  # Your rumps-based taskbar application
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'app_icon.png',  # Make sure you have app_icon.png in the same folder
    'packages': ['PyQt5', 'rumps', 'psutil'],
    'plist': {
        'CFBundleName': 'gpt4me',
        'CFBundleDisplayName': 'gpt4me',
        'CFBundleIdentifier': 'com.gpt4me.openaichat',
        'CFBundleVersion': "0.1",
        'CFBundleShortVersionString': "0.1",
        'LSUIElement': False,  # App doesn't appear in the Dock
    },
}

setup(
    name='gpt4me',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
