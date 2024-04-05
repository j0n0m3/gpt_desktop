import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class OpenAIChatApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://chat.openai.com"))
        self.setCentralWidget(self.browser)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('gpt4me')
        
        # Set the window icon to a PNG file in the same directory
        self.setWindowIcon(QIcon('app_icon.png'))  # Make sure 'app_icon.png' exists in your directory

        # Create actions for window controls
        self.createActions()

        # Create the menu bar and add actions
        self.createMenus()

        self.resize(1024, 768)  # Set initial size

    def createActions(self):
        # Minimize action
        self.minimizeAction = QAction("Minimize", self)
        self.minimizeAction.triggered.connect(self.showMinimized)

        # Maximize action
        self.maximizeAction = QAction("Maximize", self)
        self.maximizeAction.triggered.connect(self.showMaximized)

        # Close action
        self.closeAction = QAction("Close", self)
        self.closeAction.triggered.connect(self.close)

        # Zoom in action
        self.zoomInAction = QAction("Zoom In", self)
        self.zoomInAction.setShortcut(QKeySequence.ZoomIn)
        self.zoomInAction.triggered.connect(lambda: self.browser.setZoomFactor(self.browser.zoomFactor() + 0.1))

        # Zoom out action
        self.zoomOutAction = QAction("Zoom Out", self)
        self.zoomOutAction.setShortcut(QKeySequence.ZoomOut)
        self.zoomOutAction.triggered.connect(lambda: self.browser.setZoomFactor(self.browser.zoomFactor() - 0.1))

    def createMenus(self):
        menu_bar = self.menuBar()

        # Window menu
        window_menu = QMenu("Window", self)
        menu_bar.addMenu(window_menu)
        window_menu.addAction(self.minimizeAction)
        window_menu.addAction(self.maximizeAction)
        window_menu.addAction(self.zoomInAction)
        window_menu.addAction(self.zoomOutAction)
        window_menu.addAction(self.closeAction)

        # View menu for zoom actions
        view_menu = QMenu("View", self)
        menu_bar.addMenu(view_menu)
        view_menu.addAction(self.zoomInAction)
        view_menu.addAction(self.zoomOutAction)

app = QApplication(sys.argv)
app.setApplicationName('gpt4me')
window = OpenAIChatApp()
window.show()
app.exec_()
