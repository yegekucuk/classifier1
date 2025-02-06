from tensorflow.python.keras.optimizer_v2.adam import Adam
from keras.api.utils import image_dataset_from_directory
from keras.api.models import Sequential
from keras.api.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Create the model
model = Sequential()
model.add(Conv2D(64, (3, 3), input_shape=(64, 64, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
opt = Adam(learning_rate=0.01)
model.compile(optimizer="Adam", loss='binary_crossentropy', metrics=['accuracy'])

# Showing the model summary and saving the model structure
model.summary()

# Import dataset
train_set = image_dataset_from_directory(
    "dataset/trainset",
    image_size=(64, 64),
    batch_size=1,
    shuffle=True
)

test_set = image_dataset_from_directory(
    "dataset/testset",
    image_size=(64, 64),
    batch_size=1,
    shuffle=False
)

# Fit the model
model.fit(
    x=train_set,
    epochs=7,
    validation_data=test_set
)

# Save the model
model.save("model.h5")
model.save("model.keras")