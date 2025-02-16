import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from keras import models
from keras import utils
from numpy import expand_dims
from PIL import Image, ImageTk


# -- PARAMS --
image_size_last = (300,300)
model : models.Sequential
model = models.load_model("model.keras")

# -- FUNCS --
def load_image(file_path):
    # Loading the image
    img = utils.load_img(file_path, target_size=(64,64))
    img = utils.img_to_array(img)

    # Adding a dimension to the image array
    img = expand_dims(img, axis = 0)
    return img

def upload_image():
    file_path = filedialog.askopenfilename(
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png"),
    ]
)

    if file_path:
        #messagebox.showinfo("Selected File", file_path)
        #show(f"Selected File: {file_path}")
        display_image(file_path, img_canvas1)
        img = load_image(file_path)
        pred = model.predict(img)
        textPrompt = f"{pred[0][0]} "
        if int(round(pred[0][0])) == 1:
            textPrompt += "Human face"
        elif int(round(pred[0][0])) == 0:
            textPrompt += "Wild Animal"
        show(textPrompt)

    else:
        messagebox.showwarning("No File Selected", "Please select an image file.")

def show(text):
    text_area.config(state=tk.NORMAL)  # Enable writing to the text area
    text_area.delete(1.0, tk.END)  # Clear previous text
    text_area.insert(tk.END, text)  # Insert new text
    text_area.config(state=tk.DISABLED)  # Make text area read-only

def display_image(file_path, canvas):
    img = Image.open(file_path)
    img = img.resize(image_size_last, Image.Resampling.LANCZOS)  # Resize the image to fit the container
    img_tk = ImageTk.PhotoImage(img)
    
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.image = img_tk  # Keep a reference to avoid garbage collection


# -- MAIN --

# Create the main window
root = tk.Tk()
root.title("Keras CNN Classifier")
root.geometry("800x600")
root.resizable(False,False)

# Add labels for Human/Wild Cat Classifier and CNN Model
classifier_label = tk.Label(root, text="Human Wild Animal Classifier", font=("Helvetica", 18))
classifier_label.pack(pady=1)
cnn_label = tk.Label(root, text="CNN Model", font=("Helvetica", 14))
cnn_label.pack(pady=(1, 40))

# Create and place the "Upload Image" button
upload_button = tk.Button(root, text="Upload Image", command=upload_image, font=("Helvetica", 14))
upload_button.pack(pady=1)

# vBox for image
img_canvas1 = tk.Canvas(root, width=image_size_last[1], height=image_size_last[0], bg='white')
img_canvas1.pack(pady=5)

# Add a read-only text area below the image
pred_label = tk.Label(root, text="Prediction", font=("Helvetica", 11))
pred_label.pack(pady=1)
text_area = tk.Text(root, wrap=tk.WORD, height=1, width=30)
text_area.pack(pady=1)
text_area.config(state=tk.DISABLED)

# Run the application
root.mainloop()
