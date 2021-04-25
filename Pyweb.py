import sys
from PySide2 import QtCore
from PySide2.QtCore import Qt, QUrl
from PySide2.QtGui import QCloseEvent, QKeySequence, QIcon
from PySide2.QtWidgets import (QAction, QApplication, QDesktopWidget,QDockWidget, QLabel, QLineEdit, QMainWindow, QMenu, QInputDialog, QMenuBar, QPushButton,QStatusBar, QToolBar, QTabWidget)
from PySide2.QtWebEngineWidgets import (QWebEngineDownloadItem, QWebEnginePage, QWebEngineView, QWebEngineProfile)
class WebLoad(QWebEngineView):
    def __init__(self):
        super(WebLoad,self).__init__()
        self.load(QUrl('https://google.com/'))
    def prev_page(self):
        self.triggerPageAction(QWebEnginePage.Back)
    def next_page(self):
        self.triggerPageAction(QWebEnginePage.Forward)
    def reload_page(self):
        self.triggerPageAction(QWebEnginePage.Reload)
    def url_open(self):
        url = QInputDialog(self)
        value = url.getText(self, "Web URL","URL:",QLineEdit.Normal)
        self.load(QUrl('https://'+(value)[0]))
        #self.load(QUrl(url))
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('PyWeb Browser')
        self.webload = WebLoad()
        #self.qline = QLineEdit(self)
        #self.qline.setEchoMode(QLineEdit.Password)
        #self.qline.move(180,2)
        self.toolbar = QToolBar()
        self.exit_gomb = QAction(QIcon("Icons/quit.png"), "Exit")
        self.prev_gomb = QAction(QIcon("Icons/prev.png"), "Back")
        self.next_gomb = QAction(QIcon("Icons/next.png"), "Next")
        self.reload_gomb = QAction(QIcon("Icons/reload.png"), "Reload")
        self.url_gomb  = QAction(QIcon("Icons/url.png"), "Url")
        self.toolbar.addAction(self.exit_gomb)
        self.toolbar.addAction(self.prev_gomb)
        self.toolbar.addAction(self.next_gomb)
        self.toolbar.addAction(self.reload_gomb)
        self.toolbar.addAction(self.url_gomb)
        #self.qline.setMinimumSize(800,10)
        self.addToolBar(self.toolbar)
        self.exit_gomb.triggered.connect(self.exit_app)
        self.prev_gomb.triggered.connect(self.webload.prev_page)
        self.next_gomb.triggered.connect(self.webload.next_page)
        self.reload_gomb.triggered.connect(self.webload.reload_page)
        self.url_gomb.triggered.connect(self.webload.url_open)
        self.setCentralWidget(self.webload)
        #self.inputUrl()
    def exit_app(self):
        QApplication.exit()
def main():
    app = QApplication(sys.argv)
    run = MainWindow()
    run.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
