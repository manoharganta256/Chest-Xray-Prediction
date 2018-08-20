import numpy as np
from keras.preprocessing import image
from Big_Project.settings import chest_model,graph

def predict_image(path):
    test_image = image.load_img(path, target_size=(512, 512))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    # with settings.graph.as_default():
    #     result = settings.model.predict(test_image)
    # if result[0][0] == 0:
    #     prediction = 'Image consists Apple Logo'
    # else:
    #     prediction = 'Image does not contain Apple Logo'
    with graph.as_default():
        result = chest_model.predict_classes(test_image)
    probability = chest_model.predict_proba(test_image)
    probability = probability[0][0]
    if result[0][0] == 0:
        prediction = "The person doesnt have cardiomegaly"
        probability = 1-probability
    else:
        prediction = "The person has cardiomegaly"
    return prediction,probability