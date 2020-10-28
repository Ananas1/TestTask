from openni import openni2
from UI import MyAppWindow
from OniReaderClass import OniReader
from PyQt5 import QtWidgets, QtCore
import sys

path_to_file = b"./cap1.oni"

if __name__ == '__main__':
    my_player_app = QtWidgets.QApplication(sys.argv)
    window = MyAppWindow()
    window.setWindowTitle("Player for ONI files")
    window.resize(700,500)
    window.show()
    sys.exit(my_player_app.exec_())



    mydev = OniReader(path_to_file)
    limit = (mydev.get_frames_number())
    for i in range(1, limit+1, 1):
       mydev.get_frame_by_id(i)
       #mydev.save_dframe(i, mydev.get_frame_by_id(i)[0], mydev.get_frame_by_id(i)[1])
    openni2.unload()
