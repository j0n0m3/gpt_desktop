import rumps
import subprocess
import os
import psutil

class OpenAIStatusBarApp(rumps.App):
    def __init__(self):
        super(OpenAIStatusBarApp, self).__init__("🤖")
        self.menu = ["Open Chat"]
        self.chat_app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "openai_chat_app.py")
        self.init_chat_app()

    def init_chat_app(self):
        # Automatically open chat_app on startup
        self.open_chat(None)

    def app_is_running(self, process_name):
        # Check if there is any running process that contains the given name process_name.
        for proc in psutil.process_iter(['name']):
            # Check if process name contains the given name string.
            if process_name.lower() in (proc.info['name'] or '').lower():
                return True
        return False

    @rumps.clicked("Open Chat")
    def open_chat(self, _):
        # Check if chat_app.py is already running
        if not self.app_is_running('openai_chat_app.py'):
            # Run the chat_app script using Python
            subprocess.Popen(["python3", self.chat_app_path])
        else:
            rumps.alert('Chat already running.')

if __name__ == "__main__":
    OpenAIStatusBarApp().run()
