
# coding: utf-8

# In[1]:


from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D
import numpy as np
import pandas as pd


# In[2]:


(x_train,y_train),(x_test,y_test)=mnist.load_data()


# In[3]:


import matplotlib.pyplot as plt
def plot_image_lables_prediction(images,lables,prediction,idx,num=10):
    fig = plt.gcf()
    fig.set_size_inches(12,14)
    if num>25 :num=25
    for i in range(0,num):
        ax = plt.subplot(5,5,1+i)
        ax.imshow(images[idx],cmap="binary")
        title = "label="+str(lables[idx])
        if len(prediction)>0:
            title +=",prediction="+str(prediction[idx])
        ax.set_title(title,fontsize=10)
        ax.set_xticks([]);ax.set_yticks([])

        idx+=1
    plt.show()


# In[4]:


x_train4D=x_train.reshape(x_train.shape[0],28,28,1).astype("float32")
x_test4D=x_test.reshape(x_test.shape[0],28,28,1).astype("float32")


# In[5]:


x_test4D_NL=x_test4D/255
x_train4D_NL=x_train4D/255


# In[6]:


y_train_OH=np_utils.to_categorical(y_train)
y_test_OH=np_utils.to_categorical(y_test)


# In[7]:


xx = Sequential()


# In[8]:


xx=Sequential()


# In[9]:


xx.add(Conv2D(filters=16,kernel_size=(5,5),padding='same',input_shape=(28,28,1),activation="relu"))


# In[10]:


xx.add(MaxPooling2D(pool_size=(2,2)))


# In[11]:


xx.add(Conv2D(filters=36,kernel_size=(5,5),padding="same",activation='relu'))


# In[12]:


xx.add(MaxPooling2D(pool_size=(2,2)))


# In[13]:


xx.add(Dropout(0.25))


# In[14]:


xx.add(Flatten())


# In[15]:


xx.add(Dense(128,activation='relu'))


# In[16]:


xx.add(Dropout(0.5))


# In[17]:


xx.add(Dense(10,activation='softmax'))


# In[18]:


print(xx.summary())


# In[19]:


xx.compile(loss="categorical_crossentropy",optimizer='adam',metrics=['accuracy'])


# In[32]:


train_history=xx.fit(x=x_train4D_NL,y=y_train_OH,validation_split=0.2,epochs=100,batch_size=300,verbose=2)


# In[33]:


def show_train_history(train_history,train,validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel('Epoch')
    plt.legend(['train','validation'],loc='upper left')
    plt.show()


# In[34]:


show_train_history(train_history,'acc','val_acc')


# In[35]:


show_train_history(train_history,'loss','val_loss')


# In[36]:


scroes = xx.evaluate(x_test4D_NL,y_test_OH)


# In[37]:


prediction = xx.predict_classes(x_test4D_NL)


# In[38]:


prediction


# In[39]:


plot_image_lables_prediction(x_test,y_test,prediction=prediction,idx=0)


# In[40]:


pd.crosstab(y_test,prediction,rownames=["lable"],colnames=["predict"])


# In[41]:


df = pd.DataFrame({'lable':y_test,"prediction":prediction})


# In[44]:


df[(df.lable==2)&(df.prediction==7)]


# In[46]:


plot_image_lables_prediction(x_test,y_test,prediction,idx=4176,num=1)

