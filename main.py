import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

import keras_classifier1

# -- PARAMS --
image_size = (300,300)

# -- FUNCS --
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path:
        messagebox.showinfo("Selected File", file_path)
        show(f"Selected File: {file_path}")
        display_image(file_path, img_canvas1)
        img = keras_classifier1.load_image(file_path)
    else:
        messagebox.showwarning("No File Selected", "Please select an image file.")

def show(text):
    text_area.config(state=tk.NORMAL)  # Enable writing to the text area
    text_area.delete(1.0, tk.END)  # Clear previous text
    text_area.insert(tk.END, text)  # Insert new text
    text_area.config(state=tk.DISABLED)  # Make text area read-only

def display_image(file_path, canvas):
    img = Image.open(file_path)
    img = img.resize(image_size, Image.Resampling.LANCZOS)  # Resize the image to fit the container
    img_tk = ImageTk.PhotoImage(img)
    
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.image = img_tk  # Keep a reference to avoid garbage collection


# -- MAIN --

# Create the main window
root = tk.Tk()
root.title("Image Uploader")
root.geometry("800x600")
root.resizable(False,False)

# Add labels for Human/Wild Cat Classifier and CNN Model
classifier_label = tk.Label(root, text="Human/Wild Cat Classifier", font=("Helvetica", 18))
classifier_label.pack(pady=1)

cnn_label = tk.Label(root, text="CNN Model", font=("Helvetica", 14))
cnn_label.pack(pady=(1, 40))

# Create and place the "Upload Image" button
upload_button = tk.Button(root, text="Upload Image", command=upload_image, font=("Helvetica", 14))
upload_button.pack(pady=1)

pred_label = tk.Label(root, text="Prediction", font=("Helvetica", 11))
pred_label.pack(pady=1)

# Add a read-only text area below the button
text_area = tk.Text(root, wrap=tk.WORD, height=1, width=30)
text_area.pack(pady=1)
text_area.config(state=tk.DISABLED)

# Add a horizontal box (hBox) with two vertical boxes (vBox) for images under the text area
hBox = tk.Frame(root)
hBox.pack(pady=10)

# vBox for image 1
vBox1 = tk.Frame(hBox)
vBox1.pack(side=tk.LEFT, padx=10)

title1 = tk.Label(vBox1, text="Title 1", font=("Helvetica", 12))
title1.pack()

# Image container 1 using Canvas
img_canvas1 = tk.Canvas(vBox1, width=image_size[1], height=image_size[0], bg='white')
img_canvas1.pack(pady=5)

# vBox for image 2
vBox2 = tk.Frame(hBox)
vBox2.pack(side=tk.LEFT, padx=10)

title2 = tk.Label(vBox2, text="Title 2", font=("Helvetica", 12))
title2.pack()

# Image container 2 using Canvas
img_canvas2 = tk.Label(vBox2, text="Human", width=image_size[1], height=image_size[0], bg='white', font=("Helvetica", 24))
img_canvas2.pack(pady=5)

# Run the application
root.mainloop()
