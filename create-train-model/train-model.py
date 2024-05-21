from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Create an instance of ImageDataGenerator for training and testing
train_gen = ImageDataGenerator(rescale=1./255)
test_gen = ImageDataGenerator(rescale=1./255)

# Load training data
train_set = train_gen.flow_from_directory(
    "dataset", 
    target_size=(64, 64), 
    batch_size=1, 
    class_mode="binary"
)

# Load test data
test_set = test_gen.flow_from_directory(
    "testset", 
    target_size=(64, 64), 
    batch_size=1, 
    class_mode="binary"
)

# Determine the number of steps per epoch
steps_per_epoch = train_set.samples // train_set.batch_size
validation_steps = test_set.samples // test_set.batch_size

# Loading the model
model: Sequential
model = load_model("model_untrained.h5")

# Fitting the model
model.fit(
    train_set,
    steps_per_epoch=steps_per_epoch,
    epochs=10,
    validation_data=test_set,
    validation_steps=validation_steps
)

# Saving the model
model.save("model_trained.h5")