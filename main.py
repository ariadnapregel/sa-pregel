from metric import metric
from create_classifier import create_classifier
import tensorflow as tf
from ddae import training_v2
import train
import glob
import imageio

#run converter - get single frames (rgb and depth)


#load trained ddae model (nyu dataset)
autoencoder = training_v2

#create classifier model (could be pretrained) and load initial weights
model = create_classifier(classes=2, dropout_rate=0.1, shape_img=shape)

#compile classifier
model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.0001),
                        loss='binary_crossentropy',
                        metrics=['accuracy'])

# over x batches:
    #for every pair of frames:
        #autoencoder forward - get denoised depth images
        #run difodo on denoised depth images - get trajectory
        #run metric - save to a file/list/whatever whether good or bad
        #classifier forward denoised depth images - get scores for good or bad
        #loss function - compare metric and classifier results
        #backpropagate error, update all weights in ae and classifier



#run metric
label = metric(DifodoFilePath='trajectoryDIFODO.txt')

#load file that records all depth images timestep and filename
with open('depth.txt') as depth:
    images = depth.readlines()

#get path for first image
image1_path = images[1].split()[1]
image1 = imageio.imread(image1_path)
shape = image1.shape

#create classifier
model = create_classifier(classes=2, dropout_rate=0.1, shape_img=shape)

#compile classifier
model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.0001),
                        loss='binary_crossentropy',
                        metrics=['accuracy'])
#train classifier
model.fit(image1, )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
