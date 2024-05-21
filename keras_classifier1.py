from keras.preprocessing.image import image_utils
import numpy as np

def load_image(file_path):
    # Getting name of input image
    img_name = input("Please enter the full name of the image: ")

    # Loading the image
    img = image_utils.load_img(file_path, target_size=(64,64))
    img = image_utils.img_to_array(img)

    # Adding a dimension to the image array
    img = np.expand_dims(img, axis = 0)
    return img