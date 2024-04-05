import subprocess
import os

def main():
    dir_path = os.path.dirname(os.path.abspath(__file__))

    pyqt_app_path = os.path.join(dir_path, "openai_chat_app.py")
    menu_app_path = os.path.join(dir_path, "openai_menu_app.py")

    # Ensure paths are not None
    if not os.path.exists(pyqt_app_path) or not os.path.exists(menu_app_path):
        print("Error: Script paths are incorrect.")
        return

    subprocess.Popen(["python", pyqt_app_path])
    subprocess.Popen(["python", menu_app_path])

if __name__ == "__main__":
    main()
