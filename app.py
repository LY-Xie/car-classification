# -*- coding:utf-8 -*-
from flask import Flask, request, jsonify
import logging

from utils import base64_2_img
from resp import generate_error_resp, generate_success_resp
from baidu_project import test_car_type
from test_car_type import test_car_type as test
from PIL import Image

import cv2, base64
app = Flask(__name__)
app.logger.setLevel(logging.INFO)
import json

# request.data.get('base64Image', default=None)

@app.route('/test_car_type', methods=['POST'])
def check_id_card():
    data = request.data
    data = json.loads(data)
    base64_str = data['base64Image']

    base64_str = request.form.get('base64Image', default=None)
    print(after_box_ann)
    if base64_str is None:
        app.logger.warn('error: parameter base64Image is missing')
        return jsonify(generate_error_resp('base64Image'))
    img = base64_2_img(base64_str)
    result = test_car_type(img)


    result = {'car_type': car_type,'score':score}
    result = json.dumps(result)
    return jsonify(generate_success_resp(result))



if __name__ == '__main__':
    im = cv2.imread('D:/SAAS/DC/fine-grained vehicle classification/data/data/image/1/1101/2011/cf56202f4dc511.jpg')
    name, score, model_id, year = test(im)
    print(name)
    print(score)

    test_set = open('D:/SAAS/DC/fine-grained vehicle classification/data/data/train_test_split/classification/test.txt', 'r')
    test_img = test_set.readline()[0:-1]
    correct_model = 0
    correct_year = 0
    count = 0
    while test_img and count < 500:
        im = cv2.imread('D:/SAAS/DC/fine-grained vehicle classification/data/data/image/' + test_img)
        name, score, model_id, year = test(im)
        true_model_id = test_img.split('/')[1]
        true_year = test_img.split('/')[2]
        if true_model_id == model_id:
            correct_model += 1
        if true_year == year:
            correct_year += 1
        count += 1
        test_img = test_set.readline()[0:-1]
    print(correct_model / count)
    print(correct_year / count)
    print(correct_model / count * 0.8 + correct_year / count * 0.2)

    # app.run(host='0.0.0.0',port=5004)#

