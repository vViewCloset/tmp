#-*- coding: utf-8 -*-

import sys, os
import matplotlib.pyplot as plt
from matplotlib.image import imread

from keras.utils import np_utils
from keras.models import load_model
from PIL import Image
import numpy as np


f = open('../../Classify_ulf/list_category_cloth.csv','r')

while(True):
    lines = f.read().splitlines()
    if not lines:
        break

    categories = []; tmp_cat = []
    for i, d in enumerate(lines):
        tmp = lines[i]
        num_index = len(lines[i]) - 2 
        tmp_cat = tmp[:num_index]
        categories.append(tmp_cat)
        categories.sort()

f.close()

image_files = ['../../test_img/category_test/greentee.png']
#image_files = ['../category_test/stripe.jpg','../category_test/denim_pants.png','../category_test/red_dress.jpg','../category_test/red_skirt.png','../category_test/floral_skirt.png','../category_test/navy_pants.png']

image_size = 64

X = []; files = []

for fname in image_files:
    img = Image.open(fname)
    img = img.convert("RGB")
    img = img.resize((image_size, image_size))
    in_data = np.asarray(img)
    in_data = in_data.astype("float") / 256
    X.append(in_data)
    files.append(fname)

X = np.array(X)

model = load_model('../category_50/clothes_category_model_server_03.h5')

pre = model.predict(X)

for i, p in enumerate(pre):
    y = p.argmax()
    print("입력:", files[i])    # 정답
    print("예측:", "[", y, "]",categories[y], "/ Score",p[y])


