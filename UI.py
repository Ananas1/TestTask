from PyQt5 import QtWidgets, QtCore




class MyAppWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.label = QtWidgets.QLabel("This test text")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.button_open_file = QtWidgets.QPushButton("&Open file")
        self.btnQuit = QtWidgets.QPushButton("&Close app")
        self.button_fast_reverse = QtWidgets.QPushButton("&Fast reverse")
        self.button_fast_reverse.setDisabled(True)
        self.button_play = QtWidgets.QPushButton("&Play video")
        self.button_pause = QtWidgets.QPushButton("&Pause")
        self.button_pause.setDisabled(True)
        self.button_fast_forward = QtWidgets.QPushButton("&Fast forward")
        self.button_fast_forward.setDisabled(True)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button_open_file)
        self.button_open_file.clicked.connect(self.open_file)
        self.vbox.addWidget(self.button_fast_reverse)
        self.button_fast_reverse.clicked.connect(self.fast_reserve)
        self.vbox.addWidget(self.button_play)
        self.button_play.clicked.connect(self.play_video)
        self.vbox.addWidget(self.button_pause)
        self.button_pause.clicked.connect(self.set_pause)
        self.vbox.addWidget(self.button_fast_forward)
        self.button_fast_forward.clicked.connect(self.fast_forward)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
    def open_file(self):
        print('opened file')
    def fast_reserve(self):
        print('fast reserved')
    def play_video(self):
        self.button_pause.setDisabled(False)
        self.button_play.setDisabled(True)
        print('playing video')
    def set_pause(self):
        self.button_play.setDisabled(False)
        self.button_pause.setDisabled(True)
        self.button_fast_reverse.setDisabled(False)
        self.button_fast_forward.setDisabled(False)
        print('stop video')
    def fast_forward(self):
        print('fast forwarded')
