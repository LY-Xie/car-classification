# -*- coding:utf-8 -*-

def generate_error_resp(param_name):
    resp = {
        'code': 4001,
        'error': 'parameter: {} is missing'.format(param_name)
    }
    return resp

def generate_success_resp(data):
    resp = {
        'code': 200,
        'data': data
    }
    return resp
