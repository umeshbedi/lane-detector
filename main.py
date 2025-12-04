import numpy as np
import cv2
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
from tensorflow import keras
path = os.path.dirname(__file__)
print(path)
# model = keras.models.load_model('model.h5')