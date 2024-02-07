import numpy as np
from keras.preprocessing.image import image_utils 
from keras.models import load_model, Sequential
from os import system
from time import sleep

# Loading the model
model: Sequential
model = load_model("model_trained.h5")

# Clearing the warning messages
print("\nClearing the warning messages in a second! DO NOT WORRY THERE IS NO PROBLEM!")
sleep(3)
system('cls')

# Welcome message and information
print("Welcome! Use Ctrl+C to exit!")
print("This model was trained by using faces of 7159 Human face images and 4828 Wild Cat/Wolf face images. It classifys the face as Human or Wild Cat.\n")

while True:
    # Getting name of input image
    img_name = input("Please enter the full name of the image: ")

    # Loading the image
    img = image_utils.load_img(f"YOUR_IMAGES/{img_name}", target_size=(64,64))
    img = image_utils.img_to_array(img)

    # Adding a dimension to the image array
    img = np.expand_dims(img, axis = 0)

    # Getting the result
    result = model.predict(img)

    # {'animal': 0, 'human': 1}
    if result[0][0] == 1:
        result: str
        result = "human"
    elif result[0][0] == 0:
        result: str
        result = "wild cat/wolf"
    
    print(result)
