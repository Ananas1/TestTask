from PyQt5 import QtWidgets, QtCore, QtGui
from OniReaderClass import OniReader

class MyAppWindow(QtWidgets.QWidget):
    imageChange = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, parent=None):
        #super().__init__()
        super(MyAppWindow, self).__init__(parent)
        self.image_frame = QtWidgets.QLabel('This is Label widget for color frame')
        self.depth_image = QtWidgets.QLabel('This is Label widget for depth frame')

        self.button_open_file = QtWidgets.QPushButton("&Open file")
        #self.btnQuit = QtWidgets.QPushButton("&Close app")
        self.button_fast_reverse = QtWidgets.QPushButton("&Fast reverse")
        self.button_fast_reverse.setDisabled(True)
        self.button_play = QtWidgets.QPushButton("&Play video")
        self.button_pause = QtWidgets.QPushButton("&Pause")
        self.button_pause.setDisabled(True)
        self.button_fast_forward = QtWidgets.QPushButton("Fast forward")
        self.button_local_save_frames= QtWidgets.QPushButton("Save frames")
        self.button_local_save_frames.setDisabled(True)
        self.button_fast_forward.setDisabled(True)
        self.vbox = QtWidgets.QVBoxLayout()
        self.hbox_buttons = QtWidgets.QHBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.image_frame)
        self.hbox.addWidget(self.depth_image)
        self.frame_slider = QtWidgets.QSlider()
        self.frame_slider.setOrientation(QtCore.Qt.Horizontal)


        self.imageChange.connect(self.set_frame)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.frame_slider)

        self.hbox_buttons.addWidget(self.button_open_file)
        self.button_open_file.clicked.connect(self.open_file)
        self.button_play.setEnabled(False)
        self.hbox_buttons.addWidget(self.button_fast_reverse)
        self.button_fast_reverse.clicked.connect(self.fast_reserve)
        self.hbox_buttons.addWidget(self.button_play)
        self.button_play.clicked.connect(self.play_video)
        self.hbox_buttons.addWidget(self.button_pause)
        self.button_pause.clicked.connect(self.set_pause)
        self.hbox_buttons.addWidget(self.button_fast_forward)
        self.button_fast_forward.clicked.connect(self.fast_forward)
        self.hbox_buttons.addWidget(self.button_local_save_frames)
        self.button_local_save_frames.clicked.connect(self.save_frames)
        self.vbox.addLayout(self.hbox_buttons)
        #self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        #QtWidgets.QApplication.processEvents()
        #self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
        self.frame_slider.sliderMoved.connect(self.go_to_frame)
        self.show()
        #self.frame_slider.sliderReleased(self.go_to_frame)
    def open_file(self):
        filename = (QtWidgets.QFileDialog.getOpenFileName(self, 'Open2 Video', "*.oni"))[0]

        if filename :
                oni = OniReader(filename)
                self.oni = oni
                self.frame_item = 1
                self.ToStop = False
                self.button_play.setEnabled(True)
                self.button_local_save_frames.setEnabled(True)

    def read_frame_by_number(self, number_of_frame):
        type = 'color'
        self.oni.get_frame_by_id(number_of_frame)
        data_img = self.oni.get_frame_by_id(number_of_frame)[0]
        height, width, channel = data_img.shape
        bytesPerLine = 3 * width
        qImage = QtGui.QImage(data_img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        self.set_frame(qImage, type)

    def read_depth_frame_by_number(self, number_of_frame):
        type = 'depth'
        self.oni.get_frame_by_id(number_of_frame)
        data_img = self.oni.get_frame_by_id(number_of_frame)[1]
        height, width = data_img.shape
        bytesPerLine = 2 * width
        qImage = QtGui.QImage( data_img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB16)
        self.set_frame(qImage, type)

    def read_frames(self):
        self.limit = (self.oni.get_frames_number())
        for i in range(self.frame_item, self.limit + 1, 1):
            if not (self.ToStop):
                self.read_frame_by_number(i)
                self.read_depth_frame_by_number(i)
                self.frame_item += 1
                self.set_frame_slider(i)
            else:
                break

    def set_frame(self, image, type):
        pix = QtGui.QPixmap(image)
        if type == 'depth':
            self.depth_image.setPixmap(pix)
        else:
            self.image_frame.setPixmap(pix)
        QtWidgets.QApplication.processEvents()

    def set_frame_slider(self, iter):
        self.frame_slider.setMinimum(0)
        self.frame_slider.setMaximum(self.limit)
        self.frame_slider.setValue(iter)

    def go_to_frame(self):
        self.frame_item = self.frame_slider.value()
        self.ToStop = True
        self.button_play.setEnabled(True)
        self.read_frames()

    def fast_reserve(self):
        self.frame_item -= 1
        self.read_frame_by_number(self.frame_item)
        self.read_depth_frame_by_number(self.frame_item)

    def play_video(self):
        self.ToStop = False
        self.button_fast_forward.setDisabled(True)
        self.button_fast_reverse.setDisabled(True)
        self.button_pause.setDisabled(False)
        self.button_play.setDisabled(True)
        self.read_frames()

    def set_pause(self):
        self.button_play.setDisabled(False)
        self.button_pause.setDisabled(True)
        self.button_fast_reverse.setDisabled(False)
        self.button_fast_forward.setDisabled(False)
        self.ToStop = True

    def fast_forward(self):
        self.frame_item += 1
        self.read_frame_by_number(self.frame_item)
        self.read_depth_frame_by_number(self.frame_item)

    def save_frames(self):
        self.oni.save_frame(self.frame_item, self.oni.get_frame_by_id(self.frame_item)[0],self.oni.get_frame_by_id(self.frame_item)[1])