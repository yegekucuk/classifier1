from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.models import Sequential

# Creating the model
model = Sequential()

# Creating conv CNN layers
model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Flattening and adding Dense layers
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  # Çıktı katmanı, insan veya değil olarak tek bir çıktı olacak

# Compiling the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Showing the model summary and saving the model structure
model.summary()
model.save("model_untrained.h5")