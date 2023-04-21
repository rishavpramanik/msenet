import tensorflow as tf
from tensorflow.keras.models import Model

def create_model(model_name,IMG_SIZE = 256, output = 5):


    IMG_SHAPE = (IMG_SIZE, IMG_SIZE, 3)  # IMG_SIZE = 256
    if(model_name == "Xception" ):
    model = tf.keras.applications.xception.Xception(input_shape=IMG_SHAPE,
                                                          include_top=False,
                                                          weights='imagenet')
    elif(model_name == "InceptionV3"):
        model = tf.keras.applications.inception_v3.InceptionV3(input_shape=IMG_SHAPE,
                                                                        include_top=False,
                                                                        weights='imagenet')
        
    elif(model_name=="VGG"):
        model = tf.keras.applications.vgg16.VGG16(input_shape= IMG_SHAPE, 
                                                     include_top = False, 
                                                    weights='imagenet')
    else:
        return        

    x = tf.keras.layers.Flatten()(model.output)
    x = tf.keras.layers.Dense(512, activation='relu')(x)
    x = tf.keras.layers.Dense(256,activation='relu')(x)
    x = tf.keras.layers.Dense(128,activation='relu')(x)
    x = tf.keras.layers.Dense(5,activation='softmax')(x)
    model = Model(inputs=model.input, outputs=x)

    my_model = tf.keras.models.clone_model(model)
    return my_model
