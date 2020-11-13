from openni import openni2
from UI import MyAppWindow
from OniReaderClass import OniReader
from PyQt5 import QtWidgets, QtCore


if __name__ == '__main__':
    my_player_app = QtWidgets.QApplication([])
    window = MyAppWindow()
    window.setWindowTitle("Player for ONI files")
    window.setGeometry(350, 100, 1312, 606)
    #my_player_app.processEvents()
    #window.show()
    #sys.exit(my_player_app.exec_())
    my_player_app.exec_()
    openni2.unload()
