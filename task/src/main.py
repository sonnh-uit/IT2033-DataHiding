import os
import xlwt
import shutil
import cv2
import sys
import math
import numpy as np

import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path
import yaml

from lsb import LSB
from dct import DCT

def encode(init, param):
    origin_folder = init['origin_imgs_cover_dir']
    origin_img = param['cover_img']
    encoded_folder = init['encoded_imgs_dir']
    secret_message = param['secret_message']
    picture_name = param['name']

    os.chdir(origin_folder)
    lsb_img = Image.open(origin_img)
    dct_img = cv2.imread(origin_img, cv2.IMREAD_UNCHANGED)
    os.chdir("..")
    os.chdir(encoded_folder)
    lsb_img_encoded = LSB().encode_image(lsb_img, secret_message)
    dct_img_encoded = DCT().encode_image(dct_img, secret_message)
    lsb_encoded_image_file = "lsb_" + picture_name
    lsb_img_encoded.save(lsb_encoded_image_file)
    dct_encoded_image_file = "dct_" + picture_name
    cv2.imwrite(dct_encoded_image_file,dct_img_encoded)
    os.chdir("..")

def decode(init, param):
    origin_img = param['cover_img']
    decoded_folder = init['decoded_imgs_dir']
    encoded_folder = init['encoded_imgs_dir']
    picture_name = param['name']

    os.chdir(encoded_folder)
    lsb_img = Image.open("lsb_" + picture_name)
    dct_img = cv2.imread("dct_" + picture_name, cv2.IMREAD_UNCHANGED)


    os.chdir("..") #going back to parent directory

    os.chdir(decoded_folder)
    lsb_decode_img, lsb_hidden_text = LSB().decode_image(lsb_img)
    file = open("lsb_" + picture_name + ".txt","w")
    file.write(lsb_hidden_text)
    file.close()
    lsb_decode_img.save("lsb_decoded_" + picture_name)

    dct_decode_img, dct_hidden_text = DCT().decode_image(dct_img) 
    file = open("dct_" + picture_name + ".txt","w")
    file.write(dct_hidden_text) 
    file.close()
    dct_decode_img.save("dct_decoded_" + picture_name)
    os.chdir("..")



if __name__=="__main__":

    with open("variables.yaml", 'r') as variable_file:
        variables = yaml.safe_load(variable_file)
    
    test_variable = variables['test']
    init_param = variables['init']

    if not os.path.exists(init_param['encoded_imgs_dir']):
        os.makedirs(init_param['encoded_imgs_dir'])
    if not os.path.exists(init_param['decoded_imgs_dir']):
        os.makedirs(init_param['decoded_imgs_dir'])
    
    for test_case in test_variable:
        if isinstance(test_case, dict):
            encode(init_param,test_case['test_case'] )
    

    for test_case in test_variable:
        if isinstance(test_case, dict):
            decode(init_param,test_case['test_case'] )

 