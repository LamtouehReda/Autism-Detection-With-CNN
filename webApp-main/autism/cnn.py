import tensorflow as tf
import cv2

def cnn(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (200,200))
    image = image.reshape((1,200,200,3))
    model = tf.keras.models.load_model('./my_model.h5')
    predict = model.predict(image,verbose=1)
    if predict[0][0] >= 0.5:
        result = 'Autistic'
        return result
    else:
        result = 'Non_Autistic'
        return result

model = tf.keras.models.load_model('./my_model.h5')