from PyQt5 import QtWidgets, QtCore, QtGui
from OniReaderClass import OniReader
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer
from functools import partial



class MyAppWindow(QtWidgets.QWidget):
    imageChange = QtCore.pyqtSignal(QtGui.QImage)


    def __init__(self, parent=None):
        super().__init__()
        super(MyAppWindow, self).__init__(parent)
        #self.label = QtWidgets.QLabel("This test text")

        #self.label.setAlignment(QtCore.Qt.AlignHCenter)
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


        self.scene = QtWidgets.QGraphicsScene()
        self.viewer = QtWidgets.QGraphicsView()
        self.vbox.addWidget(self.viewer)


        #self.scene.sceneRect()


        self.item = QtWidgets.QGraphicsPixmapItem()
        self.viewer.setScene(self.scene)

        #self.viewer.setScene(self.scene)

        self.scene.addItem(self.item)
        self.imageChange.connect(self.set_frame)

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


    #def paintEvent(self, event):
    #   QtWidgets.QWidget.pa

    def open_file(self):
        filename = (QtWidgets.QFileDialog.getOpenFileName(self, 'Open2 Video'))[0]
        oni = OniReader(filename)
        self.oni = oni
        self.frame_item = 0
        self.Tostop = False
    def read_frames(self):
        print('reading')
        print(self.frame_item)
        limit = (self.oni.get_frames_number())
        for i in range(self.frame_item, limit + 1, 1):
            if not (self.Tostop):
                self.oni.get_frame_by_id(i)
                data_img = self.oni.get_frame_by_id(i)[0]
                height, width, channel = data_img.shape
                bytesPerLine = 3 * width
                qImage = QtGui.QImage(data_img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
                print(f'something doing {i}')
                self.imageChange.emit(qImage)
                self.frame_item += 1
                print(self.frame_item)
            else:
                break

            #QtWidgets.QApplication.processEvents()
            #self.scene.changed.connect(partial(self.set_frame, qImage))

    def set_frame(self, image):


        #self.scene.clear()
        pix = QtGui.QPixmap(image)
        print('set frame')
        self.item = QtWidgets.QGraphicsPixmapItem(pix)
       # self.item.setPixmap(pix)
        #QtCore.QThread.msleep(5)
        self.scene.addItem(self.item)
        self.viewer.repaint()
        QtWidgets.QApplication.processEvents()
        #self.viewer.setScene(self.scene)
        #self.scene.addPixmap(pix)
        #.QThread.msleep(1000)
        #self.scene.update()
        #self.viewer.update()
        #QtCore.QThread.msleep(1000)
        #self.viewer.setFrameRect()
        #self.viewer.update()
        #self.scene.render()
        #self.viewer.update(self.scene)

        #self.scene.changed.connect(self.fast_reserve)

    def fast_reserve(self):
        print('fast reserved')

    def play_video(self):

        self.Tostop = False
        print(self.Tostop)
        self.button_pause.setDisabled(False)
        self.button_play.setDisabled(True)
        print(self.item)
        self.read_frames()




    def set_pause(self):
        #self.oni.get_frame_by_id(5)
        #self.oni.save_dframe(5, self.oni.get_frame_by_id(5)[0], self.oni.get_frame_by_id(5)[1])
        self.button_play.setDisabled(False)
        self.button_pause.setDisabled(True)
        self.button_fast_reverse.setDisabled(False)
        self.button_fast_forward.setDisabled(False)
        self.Tostop = True
        print(self.item)

        print('stop video')

    def fast_forward(self):
        print('fast forwarded')
