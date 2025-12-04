from scipy.misc import imresize
import numpy as np
from tensorflow import keras
import os
path = os.path.dirname(__file__)
model = keras.models.load_model('model.h5')

class Lanes():
    def __init__(self):
        self.recent_fit = []
        self.avg_fit = []  # average over the last n fits

    def road_lines(self, image):
        small_img = imresize(image, (80, 160, 3))
        small_img = np(small_img)
        small_img = small_img[None, :, :, :]  # shape (1, 80, 160, 3)
        
        predction = ""