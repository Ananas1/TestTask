from openni import openni2
import numpy as np
import matplotlib.pyplot as plt

class OniReader:
    def __init__(self,path):
        openni2.initialize()
        self.__dev = openni2.Device.open_file(path.encode('utf-8'))
        self.__color = self.__dev.create_color_stream()
        self.__depth = self.__dev.create_depth_stream()
        self.__number_of_dframes = self.__depth.get_number_of_frames()
    def get_frames_number(self):
        print(f'Число img кадров {self.__color.get_number_of_frames()}')
        print(f'Число depth кадров {self.__depth.get_number_of_frames()}')
        return self.__number_of_dframes
    def get_frame_by_id(self, frame_id):
        self.__color.start()
        self.__depth.start()
        pbs = openni2.PlaybackSupport(self.__dev)
        pbs.seek(self.__depth, frame_id)
        dframe = self.__depth.read_frame()
        cframe = self.__color.read_frame()
        img = np.ndarray((cframe.height, cframe.width, 3), dtype=np.uint8, buffer=cframe.get_buffer_as_triplet())
        dimg = np.ndarray((dframe.height, dframe.width), dtype=np.uint16, buffer=dframe.get_buffer_as_uint16())
        self.__color.stop()
        self.__depth.stop()
        return img, dimg
    def save_dframe(self,iter, gotten_cframe, gotten_dframe):
        plt.imsave(f"dimg_new_{iter}.png", gotten_dframe)
        plt.imsave(f"img_new_{iter}.png", gotten_cframe)
