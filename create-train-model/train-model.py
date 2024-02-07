from keras.models import load_model, Sequential
from keras.preprocessing.image import ImageDataGenerator

# Creating the image generators for training and testing
train_gen = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)
test_gen = ImageDataGenerator(rescale = 1./255)

# Generating the training and testing datasets using the generators
train_set = train_gen.flow_from_directory("dataset", target_size = (64,64), batch_size = 1, class_mode = "binary")
test_set1 = test_gen.flow_from_directory("test-set_preprocessed", target_size = (64,64), batch_size = 1, class_mode = "binary")


print(train_set.class_indices)
print(test_set1.class_indices)
raise KeyError

# Loading the model
model: Sequential
model = load_model("model_untrained.h5")

# Fitting the model
model.fit_generator(train_set,steps_per_epoch=11987,epochs=2,validation_data=test_set1,validation_steps=120)

# Saving the model
model.save("model_trained.h5")