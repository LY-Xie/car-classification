import requests,os,cv2,json,base64

url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/car'
# url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/redwine'
appid = '18099681'
key = 'yq76bfxT90t2dThVXGAkMaan'
secret_key = 'xHGlpKY57iw1co0ETkITOtIrLcVLppVo'


def test_car_type(img):
    h, w, _ = img.shape
    if w<=50 or h<=50:
        img = cv2.resize(img,(w*2,h*2))
    else:
        new_h = 200
        new_w = int(w*new_h/h)
        img = cv2.resize(img, (new_w, new_h))
    cv2.imwrite('1.png',img)
    with open("1.png", 'rb') as f:
        base64_data = base64.b64encode(f.read())
        img_data = base64_data.decode()
    token_url = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={key}&client_secret={secret_key}'
    token_res = requests.get(token_url)
    access_token = json.loads(token_res.text)['access_token']
    data = {'Content-Type': 'application/x-www-form-urlencoded', 'image': img_data, 'access_token': access_token}
    res = requests.post(url, data)
    out = json.loads(res.text)['result'][0]
    return out