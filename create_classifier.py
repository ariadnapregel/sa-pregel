import tensorflow as tf

def create_classifier(classes=2, dropout_rate=0.1, shape_img):
    input = tf.keras.layers.Input(shape=shape_img)

    # convolutional layers
    x = tf.keras.layers.Conv2D(filters=32, kernel_size=3, strides=1)(input)
    x = tf.keras.layers.Dropout(dropout_rate)(x)  #
    x = tf.keras.layers.BatchNormalization()(x)  #
    x = tf.keras.layers.Activation('relu')(x)

    x = tf.keras.layers.Conv2D(filters=64, kernel_size=3, strides=1)(input)
    x = tf.keras.layers.Dropout(dropout_rate)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation('relu')(x)

    x = tf.keras.layers.Conv2D(filters=128, kernel_size=3, strides=2)(input)
    x = tf.keras.layers.Dropout(dropout_rate)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation('relu')(x)

    x = tf.keras.layers.Conv2D(filters=256, kernel_size=3, strides=2)(input)
    x = tf.keras.layers.Dropout(dropout_rate)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation('relu')(x)

    x = tf.keras.layers.Conv2D(filters=512, kernel_size=3, strides=2)(input)
    x = tf.keras.layers.Dropout(dropout_rate)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation('relu')(x)

    x = tf.keras.layers.GlobalMaxPooling2D()(x)

    # dense layers
    x = tf.keras.layers.Dropout(dropout_rate)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Dense(units=64)(x)
    x = tf.keras.layers.Activation('relu')(x)

    x = tf.keras.layers.Dropout(dropout_rate)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Dense(units=classes)(x)
    predictions = tf.keras.layers.Activation('softmax')(x)

    model = tf.keras.Model(imputs=input, outputs=predictions)

    print(model.summary())
    print(f'Total number of layers: {len(model.layers)}')

    return model


if __name__ == '__main__':
    #shape_img = (720, 1280)
    create_classifier(classes=2, dropout_rate=0.1, shape_img)
