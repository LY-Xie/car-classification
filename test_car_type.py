import cv2,os,random,time
from keras.models import load_model
from keras.applications import imagenet_utils
import numpy as np
from scipy.io import loadmat


preprocess_input = lambda x: imagenet_utils.preprocess_input(x, mode='torch')
make_names = loadmat('make_model_name.mat')['make_names']
model_names = loadmat('make_model_name.mat')['model_names']

model = load_model('models/final.h5',compile=False)
_ = model.predict(np.zeros((1,64,64,3)))
print('model is ready !!!')

class_name = []
with open('train.txt','r') as f:
    data = f.readlines()
for i in data:
    img_name, class_ = i.strip().split(',')
    if class_ not in class_name:
        class_name.append(class_)

def get_make_name(num):
    try:
        res = make_names[num][0][0]
    except:
        res = make_names[num][0]
    return res

def get_model_name(num):
    try:
        res = model_names[int(num)][0][0]
    except:
        res = model_names[int(num)][0]
    return res



def test_car_type(img):
    h, w, _ = img.shape
    if w > h and w > 600:
        new_w = 600
        new_h = h * 600 // w
        img = cv2.resize(img, (new_w, new_h))
        h, w, _ = img.shape
    elif h > w and h > 600:
        new_h = 600
        new_w = w * 600 // h
        img = cv2.resize(img, (new_w, new_h))
        h, w, _ = img.shape


    img = preprocess_input(np.expand_dims(img, axis=0))
    res = model.predict(img)
    num = np.argmax(res[0])
    score = round(res[0][num], 3)
    name = class_name[int(num)]
    make_id, model_id, year = name.split('_')
    after_name = f'{get_make_name(int(make_id)-1)},{get_model_name(int(model_id)-1)},{year}'
    return after_name,str(round(score,3)), model_id, year



