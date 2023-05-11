import os
from keras.models import load_model
import keras.utils as image
import numpy as np
from django.conf import settings

path = os.path.join(settings.STATIC_ROOT, "DeepVision", "classifier.h5")
print(path)
model=load_model(path)
print("model loaded")


def predict(path):
    target_size = (256,256)
    test_image = image.load_img(path, target_size = target_size)
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = model.predict(test_image)

    if result[0][0] == 1:
        return "Glaucoma"
    else:
        return "Not Glaucoma"