from django.shortcuts import render
from django.http import JsonResponse

from keras._tf_keras.keras.models import load_model, Sequential
from keras._tf_keras.keras import utils

from numpy import expand_dims
import os
import tempfile

def index(request):
    return render(request, 'index.html')

def make_prediction(request):
    if request.method == 'POST' and request.FILES['image']:
        # Save img to temporary file
        image_file = request.FILES['image']
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(image_file.read())
        temp_file.close()

        # Load model
        model: Sequential = load_model("model.keras")
        model.compile(optimizer="Adam", loss='categorical_crossentropy', metrics=['accuracy'])

        # Image preprocessing
        img = utils.load_img(temp_file.name, target_size=(64, 64))
        img = utils.img_to_array(img)
        img = expand_dims(img, axis=0)

        # Make predictions
        pred = model.predict(img)
        textPrompt = f"{pred[0][0]:.4f} - "
        if int(round(pred[0][0])) == 1:
            textPrompt = "Human face"
        else:
            textPrompt = "Wild Animal"

        # Delete the temp file
        os.remove(temp_file.name)

        return JsonResponse({'prediction': textPrompt})
    return JsonResponse({'error': 'No image provided'}, status=400)
