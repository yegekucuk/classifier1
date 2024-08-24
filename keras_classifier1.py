#from keras.preprocessing.image import image_utils
from tensorflow.keras import utils
import numpy as np

def load_image(file_path):
    # Loading the image
    img = utils.load_img(file_path, target_size=(64,64))
    img = utils.img_to_array(img)

    # Adding a dimension to the image array
    img = np.expand_dims(img, axis = 0)
    return img