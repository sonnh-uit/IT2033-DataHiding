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

    os.chdir(origin_folder)
    lsb_img = Image.open(origin_img)
    dct_img = cv2.imread(origin_img, cv2.IMREAD_UNCHANGED)
    print("Description : ",lsb_img,"\nMode : ", lsb_img.mode)
    print("The message length is: ",len(secret_message))
    os.chdir("..")
    os.chdir(encoded_folder)
    lsb_img_encoded = LSB().encode_image(lsb_img, secret_message)
    dct_img_encoded = DCT().encode_image(dct_img, secret_message)
    lsb_encoded_image_file = "lsb_" + origin_img
    lsb_img_encoded.save(lsb_encoded_image_file)
    dct_encoded_image_file = "dct_" + origin_img
    cv2.imwrite(dct_encoded_image_file,dct_img_encoded)
    print("Encoded images were saved!")
    os.chdir("..")

def decode(init, param):
    origin_img = param['cover_img']
    decoded_folder = init['decoded_imgs_dir']
    encoded_folder = init['encoded_imgs_dir']


    os.chdir(encoded_folder)
    lsb_img = Image.open("lsb_" + origin_img)
    dct_img = cv2.imread("dct_" + origin_img, cv2.IMREAD_UNCHANGED)


    os.chdir("..") #going back to parent directory


    os.chdir(decoded_folder)
    # lsb_decode_img, lsb_hidden_text = LSB().decode_image(lsb_img)
    # file = open("lsb_" + origin_img + ".txt","w")
    # file.write(lsb_hidden_text)
    # file.close()
    # lsb_decode_img.save("lsb_decoded_" + origin_img)



    dct_decode_img, dct_hidden_text = DCT().decode_image(dct_img) 
    file = open("dct_" + origin_img + ".txt","w")
    file.write(dct_hidden_text) 
    file.close()
    dct_decode_img.save("dct_decoded_" + origin_img)
    #  saving hidden text as text file
    
    
    
    # print("Hidden texts were saved as text file!")
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
            decode(init_param,test_case['test_case'] )
            # os.chdir(init_param['origin_imgs_cover_dir'])
            # original_image_file = test_case['test_case']['cover_img']
            # lsb_img = Image.open(original_image_file)
            # dct_img = cv2.imread(original_image_file, cv2.IMREAD_UNCHANGED)
            # print("Description : ",lsb_img,"\nMode : ", lsb_img.mode)
            # secret_msg = test_case['test_case']['secret_message']
            # print("The message length is: ",len(secret_msg))
            # os.chdir("..")
            # os.chdir(init_param['encoded_imgs_dir'])
            # lsb_img_encoded = LSB().encode_image(lsb_img, secret_msg)
            # dct_img_encoded = DCT().encode_image(dct_img, secret_msg)
            # lsb_encoded_image_file = "lsb_" + original_image_file
            # lsb_img_encoded.save(lsb_encoded_image_file)
            # dct_encoded_image_file = "dct_" + original_image_file
            # cv2.imwrite(dct_encoded_image_file,dct_img_encoded)
            # print("Encoded images were saved!")
            # os.chdir("..")

    
    



    # while True:
    #     m = input("To encode press '1', to decode press '2', to compare press '3', press any other button to close: ")

    #     if m == "1":
    #         os.chdir("Original_image/")
    #         original_image_file = input("Enter the name of the file with extension : ")
    #         lsb_img = Image.open(original_image_file)
    #         dct_img = cv2.imread(original_image_file, cv2.IMREAD_UNCHANGED)
    # #        dwt_img = cv2.imread(original_image_file, cv2.IMREAD_UNCHANGED)
    #         print("Description : ",lsb_img,"\nMode : ", lsb_img.mode)
    #         secret_msg = input("Enter the message you want to hide: ")
    #         print("The message length is: ",len(secret_msg))
    #         os.chdir("..")
    #         os.chdir("Encoded_image/")
    #         lsb_img_encoded = LSB().encode_image(lsb_img, secret_msg)
    #         dct_img_encoded = DCT().encode_image(dct_img, secret_msg)
    # #        dwt_img_encoded = DWT().encode_image(dwt_img, secret_msg)
    #         lsb_encoded_image_file = "lsb_" + original_image_file
    #         lsb_img_encoded.save(lsb_encoded_image_file)
    #         dct_encoded_image_file = "dct_" + original_image_file
    #         cv2.imwrite(dct_encoded_image_file,dct_img_encoded)
    # #        dwt_encoded_image_file = "dwt_" + original_image_file
    # #        cv2.imwrite(dwt_encoded_image_file,dwt_img_encoded) # saving the image with the hidden text
    #         print("Encoded images were saved!")
    #         os.chdir("..")

    #     elif m == "2":
    #         os.chdir("Encoded_image/")
    #         lsb_img = Image.open(lsb_encoded_image_file)
    #         dct_img = cv2.imread(dct_encoded_image_file, cv2.IMREAD_UNCHANGED)
    # #        dwt_img = cv2.imread(dwt_encoded_image_file, cv2.IMREAD_UNCHANGED)
    #         os.chdir("..") #going back to parent directory
    #         os.chdir("Decoded_output/")
    #         lsb_hidden_text = LSB().decode_image(lsb_img)
    #         dct_hidden_text = DCT().decode_image(dct_img) 
    # #        dwt_hidden_text = DWT().decode_image(dwt_img) 
    #         file = open("lsb_hidden_text.txt","w")
    #         file.write(lsb_hidden_text) # saving hidden text as text file
    #         file.close()
    #         file = open("dct_hidden_text.txt","w")
    #         file.write(dct_hidden_text) # saving hidden text as text file
    #         file.close()
    # #        file = open("dwt_hidden_text.txt","w")
    # #        file.write(dwt_hidden_text) # saving hidden text as text file
    # #        file.close()
    #         print("Hidden texts were saved as text file!")
    #         os.chdir("..")
    #     elif m == "3":
    #         #comparison calls
    #         os.chdir("Original_image/")
    #         original = cv2.imread(original_image_file)
    #         os.chdir("..")
    #         os.chdir("Encoded_image/")
    #         lsbEncoded = cv2.imread(lsb_encoded_image_file)
    #         dctEncoded = cv2.imread(dct_encoded_image_file)
    # #        dwtEncoded = cv2.imread(dwt_encoded_image_file)
    #         original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    #         lsb_encoded_img = cv2.cvtColor(lsbEncoded, cv2.COLOR_BGR2RGB)
    #         dct_encoded_img = cv2.cvtColor(dctEncoded, cv2.COLOR_BGR2RGB)
    # #        dwt_encoded_img = cv2.cvtColor(dwtEncoded, cv2.COLOR_BGR2RGB)
    #         os.chdir("..")
    #         os.chdir("Comparison_result/")

    #         book = xlwt.Workbook()
    #         sheet1=book.add_sheet("Sheet 1")
    #         style_string = "font: bold on , color red; borders: bottom dashed"
    #         style = xlwt.easyxf(style_string)
    #         sheet1.write(0, 0, "Original vs", style=style)
    #         sheet1.write(0, 1, "MSE", style=style)
    #         sheet1.write(0, 2, "PSNR", style=style)
    #         sheet1.write(1, 0, "LSB")
    #         sheet1.write(1, 1, Compare().meanSquareError(original, lsb_encoded_img))
    #         sheet1.write(1, 2, Compare().psnr(original, lsb_encoded_img))
    #         sheet1.write(2, 0, "DCT")
    #         sheet1.write(2, 1, Compare().meanSquareError(original, dct_encoded_img))
    #         sheet1.write(2, 2, Compare().psnr(original, dct_encoded_img))
    #         sheet1.write(3, 0, "DWT")
    # #        sheet1.write(3, 1, Compare().meanSquareError(original, dwt_encoded_img))
    # #        sheet1.write(3, 2, Compare().psnr(original, dwt_encoded_img))

    #         book.save("Comparison.xls")
    #         print("Comparison Results were saved as xls file!")
    #         os.chdir("..")
    #     else:
    #         print("Closed!")
    #         break