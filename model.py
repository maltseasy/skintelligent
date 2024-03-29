from tensorflow import keras
from tensorflow.keras import layers
import tensorflow as tf
learn_rate = 0.00001
loss_list = ["categorical_crossentropy",'categorical_crossentropy',
'categorical_crossentropy','categorical_crossentropy',
'categorical_crossentropy']

test_metrics = {'a': 'accuracy','c': 'accuracy',
               'p': 'accuracy','u': 'accuracy',
               'w': 'accuracy'}
"""
def CNN_model(x,y,z):
    inputs = keras.Input(shape=(x,y,z), name='input')
    x = layers.Conv2D(16,5, activation='relu')(inputs)
    x = layers.MaxPooling2D(2)(x)
    x = layers.Dropout(0.2)(x)
    x = layers.Conv2D(32, 5, activation='relu')(x)
    x = layers.MaxPooling2D(2)(x)
    x = layers.Dropout(0.2)(x)
    x = layers.Conv2D(64, 5, activation='relu')(x)
    x = layers.MaxPooling2D(2)(x)
    x = layers.Dropout(0.25)(x)
    x = layers.Conv2D(64, 5, activation='relu')(x)
    x = layers.MaxPooling2D(2)(x)
    x = layers.Dropout(0.25)(x)
    x = layers.Flatten()(x)
    x = layers.Dense(128, activation='relu')(x)
    x = layers.Dropout(0.2)(x)
    x = layers.Dense(64, activation='relu')(x)
    x = layers.Dropout(0.2)(x)
    outputs = layers.Dense(5, activation='sigmoid', name='output')(x)
    
    model = keras.Model(inputs, outputs, name='cnn_model')
    model.compile(optimizer=keras.optimizers.Adam(learn_rate),
        loss='binary_crossentropy',
        metrics=['accuracy'])
    return model
"""
"""
def CNN_model_sec(x,y,z):
    inputs = keras.Input(shape=(x,y,z), name='input')

    x = layers.Conv2D(16,(3,3), padding='same', activation='relu')(inputs)
    x = layers.Conv2D(32, (3,3), activation='relu')(x)
    x = layers.MaxPooling2D((2,2))(x)
    x = layers.Dropout(0.25)(x)

    x = layers.Conv2D(32, (3,3), padding='same', activation='relu')(x)
    x = layers.Conv2D(64, (3,3), activation='relu')(x)
    x = layers.MaxPooling2D((2,2))(x)
    x = layers.Dropout(0.25)(x)

    x = layers.Flatten()(x)
    x = layers.Dense(128, activation='relu')(x)
    x = layers.Dropout(0.5)(x)
    x = layers.Dense(64, activation='relu')(x)
    x = layers.Dropout(0.5)(x)
    outputs = layers.Dense(2, activation='sigmoid', name='output')(x)
    
    model = keras.Model(inputs, outputs, name='cnn_model')
    model.compile(optimizer=keras.optimizers.Adam(learn_rate),
        loss='binary_crossentropy',
        metrics=['accuracy'])
    return model
"""
# def CNN_model_sec(x,y,z):
#     inputs = keras.Input(shape=(x,y,z), name='input')
#     x = layers.Conv2D(32, (3,3), activation='relu', padding='same', name='Conv1_1')(inputs)
#     x = layers.Conv2D(32, (3,3), activation='relu', padding='same', name='Conv1_2')(x)
#     x = layers.MaxPooling2D((2,2), name='pool1')(x)
    
#     x = layers.SeparableConv2D(64, (3,3), activation='relu', padding='same', name='Conv2_1')(x)
#     x = layers.SeparableConv2D(64, (3,3), activation='relu', padding='same', name='Conv2_2')(x)
#     x = layers.MaxPooling2D((2,2), name='pool2')(x)
    
#     x = layers.SeparableConv2D(128, (3,3), activation='relu', padding='same', name='Conv3_1')(x)
#     x = layers.BatchNormalization(name='bn1')(x)
#     x = layers.SeparableConv2D(128, (3,3), activation='relu', padding='same', name='Conv3_2')(x)
#     x = layers.BatchNormalization(name='bn2')(x)
#     x = layers.SeparableConv2D(128, (3,3), activation='relu', padding='same', name='Conv3_3')(x)
#     x = layers.MaxPooling2D((2,2), name='pool3')(x)
    
#     x = layers.SeparableConv2D(256, (3,3), activation='relu', padding='same', name='Conv4_1')(x)
#     x = layers.BatchNormalization(name='bn3')(x)
#     x = layers.SeparableConv2D(256, (3,3), activation='relu', padding='same', name='Conv4_2')(x)
#     x = layers.BatchNormalization(name='bn4')(x)
#     x = layers.SeparableConv2D(256, (3,3), activation='relu', padding='same', name='Conv4_3')(x)
#     x = layers.MaxPooling2D((2,2), name='pool4')(x)
    
#     x = layers.Flatten(name='flatten')(x)
#     x = layers.Dense(512, activation='relu', name='fc1')(x)
#     x = layers.Dropout(0.3, name='dropout1')(x)
#     x = layers.Dense(256, activation='relu', name='fc2')(x)
#     x = layers.Dropout(0.3, name='dropout2')(x)
#     outputs = layers.Dense(2, activation='sigmoid', name='fc3')(x)

#     model = keras.Model(inputs, outputs, name='cnn_model')
#     model.compile(optimizer=keras.optimizers.Adam(learn_rate),
#         loss='categorical_crossentropy',
#         metrics=['accuracy'])

#     return model
def CNN_model(x,y,z):
    base_model = tf.keras.applications.ResNet50(input_shape=(x, y, z),
                                               include_top=False)
    # for layer in base_model.layers[:-23]:
    #     layer.trainable = False
    
    model = tf.keras.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.5),
        
        layers.Dense(5, activation='softmax')
        ])
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=learn_rate, beta_2=0.9999, epsilon=1e-08),
        loss='categorical_crossentropy',
        metrics=['accuracy'])
    
    return model

def CNN_model_sec(x,y,z):
    base_model = tf.keras.applications.ResNet50(input_shape=(x, y, z),
                                               include_top=False)
    # for layer in base_model.layers[:-23]:
    #     layer.trainable = False
   
    model = tf.keras.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.35),
        layers.Dense(3, activation='softmax')
        ])
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=learn_rate, beta_2=0.9999, epsilon=1e-08),
        loss='categorical_crossentropy',
        metrics=['accuracy'])
    
    return model

def multi_model(x,y,z,loss_list,test_metrics,dd):
    
    base_model = tf.keras.applications.VGG19(weights='imagenet', include_top=False)

    #freeze all the layers
    for layer in base_model.layers[:]:
       layer.trainable = False

    
    model_input = keras.Input(shape=(x, y, z))
    x = base_model(model_input)
    x = layers.GlobalAveragePooling2D()(x)
    
    # let's add a fully-connected layer
    x = layers.Dense(256, activation='relu')(x)
    x = layers.Dropout(dd)(x)
    x = layers.Dense(256, activation='relu')(x)
    x = layers.Dropout(dd)(x)
    # start passing that fully connected block output to all the 
    # different model heads
    y1 = layers.Dense(128, activation='relu')(x)
    y1 = layers.Dropout(dd)(y1)
    y1 = layers.Dense(64, activation='relu')(y1)
    y1 = layers.Dropout(dd)(y1)
    
    y2 = layers.Dense(128, activation='relu')(x)
    y2 = layers.Dropout(dd)(y2)
    y2 = layers.Dense(64, activation='relu')(y2)
    y2 = layers.Dropout(dd)(y2)
    
    y3 = layers.Dense(128, activation='relu')(x)
    y3 = layers.Dropout(dd)(y3)
    y3 = layers.Dense(64, activation='relu')(y3)
    y3 = layers.Dropout(dd)(y3)

    y4 = layers.Dense(128, activation='relu')(x)
    y4 = layers.Dropout(dd)(y4)
    y4 = layers.Dense(64, activation='relu')(y4)
    y4 = layers.Dropout(dd)(y4)
    
    y5 = layers.Dense(128, activation='relu')(x)
    y5 = layers.Dropout(dd)(y5)
    y5 = layers.Dense(64, activation='relu')(y5)
    y5 = layers.Dropout(dd)(y5)
    
    #connect all the heads to their final output layers
    y1 = layers.Dense(3, activation='softmax',name= 'a')(y1)
    y2 = layers.Dense(3, activation='softmax',name= 'c')(y2)
    y3 = layers.Dense(3, activation='softmax',name= 'p')(y3)
    y4 = layers.Dense(3, activation='softmax',name= 'u')(y4)
    y5 = layers.Dense(3, activation='softmax',name= 'w')(y5)
    
    model = keras.Model(inputs=model_input, outputs=[ y1, y2, y3, y4, y5])
    
    model.compile(loss=loss_list, optimizer=keras.optimizers.SGD(lr=learn_rate,momentum=0.9), metrics=test_metrics)

    return model

if __name__ == '__main__':
    print("Model contained within this script.")
