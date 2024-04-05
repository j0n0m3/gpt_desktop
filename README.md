# gpt_standalone
This will connect to chat.openai to access within a standalone container on your desktop

Run cmds:
pip install -r requirements.txt  # Install required packages
rm -rf build dist                # Clean previous builds
python setup.py py2app           # Build the app
