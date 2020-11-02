from openni import openni2
from UI import MyAppWindow
from OniReaderClass import OniReader
from PyQt5 import QtWidgets, QtCore


if __name__ == '__main__':
    my_player_app = QtWidgets.QApplication([])
    window = MyAppWindow()
    window.setWindowTitle("Player for ONI files")
    window.resize(700,1000)
    #my_player_app.processEvents()
    #window.show()
    #sys.exit(my_player_app.exec_())
    my_player_app.exec_()



    #apath_to_file = path_to_file.encode('utf-8')
    #mydev = OniReader(apath_to_file)
    #limit = (mydev.get_frames_number())
    #for i in range(1, limit+1, 1):
       #mydev.get_frame_by_id(i)
  # mydev.save_dframe(i, mydev.get_frame_by_id(i)[0], mydev.get_frame_by_id(i)[1])
    #oni = OniReader(path_to_file)
    #a=(oni.get_frame_by_id(5)[0])
    #b=(oni.get_frame_by_id(5)[1])
    #c = np.concatenate((a,b), )
    openni2.unload()
