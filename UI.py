import sys
from PyQt5 import  QtWidgets,QtCore

from openni import openni2

class MyPlayerWindow(QtWidgets.QMainWindow):
    def __init__(self,title):
        super().__init__()
        self.setGeometry(350,350,350, 350)
        self.init_ui_elements(title)


    def init_ui_elements(self, title):
        self.setWindowTitle(title)
        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        open_file = QtWidgets.QAction('Open', self)
        open_file.setShortcut("Ctrl+O")
        open_file.setStatusTip("Open new file")
        open_file.triggered.connect(self.show_open_file())
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(self.show_open_file())
        self.setGeometry(300,300,350,350)
        self.setWindowTitle('File dialog')
        self.show()
        ##self.btnPlay = QtWidgets.QPushButton("&Play video")
        #self.init_ui_elements()
        #self.vbox = QtWidgets.QVBoxLayout()
        #self.vbox.addWidget(self.btnPlay)
       ## self.setLayout(self.vbox)
        #openBtn = QtWidgets.QPushButton('Open Video')
        #openBtn.clicked.connect(self.open_file)


    def rerutn_file_path(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        f = open(filename, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)

        #self.mediaPlayer.setMedia(QtWidgets.QMediaContent(QtCore.QUrl.fromLocalFile((filename[0]))))
        #self.playBtn.setEnabled(True)





