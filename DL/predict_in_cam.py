
# coding: utf-8

# In[3]:


from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import decode_predictions
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from keras.applications.vgg16 import preprocess_input
import numpy as np
import argparse
import cv2
model = VGG16()


# In[4]:


model = VGG16()

# In[21]:
cap = cv2.VideoCapture(0)

while(cap.read()):
	_,frame = cap.read()
	img_file='img/this.jpg'
	# load an image from file
	cv2.imwrite(img_file, frame)
	orig = cv2.imread(img_file)


	image = load_img(img_file, target_size=(224, 224))
	# convert the image pixels to a numpy array
	image = img_to_array(image)
	# reshape data for the model
	image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
	# prepare the image for the VGG model
	image = preprocess_input(image)
	# predict the probability across all output classes
	yhat = model.predict(image)
	# convert the probabilities to class labels
	label = decode_predictions(yhat)
	# retrieve the most likely result, e.g. highest probability
	label = label[0][0]
	# print the classification
	print('%s (%.2f%%)' % (label[1], label[2]*100))
	cv2.putText(orig, "{}: {} %".format(label[1],label[2]), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
	cv2.imshow("Classification", orig)
	if cv2.waitKey(1) & 0xFF == 27:
            break


