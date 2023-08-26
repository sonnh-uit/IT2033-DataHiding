import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image
u=3.57
x_k=0.45647
x=[]
def ReadImage(name):
    img=cv2.imread(name)
    return img
def ChaoticsMap(u0,x0,s):
    x.append(x0)
    for i in range (1,s):
        y=np.float16((u0*x[i-1]*(1-x[i-1])*pow(2,12))%1)
        x.append(y)
def embedding_position_matrix(x, M, N):
    y=np.empty((len(x), 3), dtype=int)
    for i in range (0,len(x)):
        y1=math.floor((x[i]-1)/(M*N))
        y2=(x[i]-1)%N
        y3=(math.floor((x[i]-1)/M))%N
        y[i][2]=y1
        y[i][0]=y2
        y[i][1]=y3
    return y
def lsb(y,message,img):
    binary_string = ''.join(format(ord(char), '08b') for char in message)
    for i in range(0,len(binary_string)):
        if binary_string[i]=='1':
            if img[y[i][0],y[i][1],y[i][2]]%2==0:
                img[y[i][0],y[i][1],y[i][2]]=img[y[i][0],y[i][1],y[i][2]]+1
        if binary_string[i]=='0':
            if img[y[i][0],y[i][1],y[i][2]]%2==1:
                img[y[i][0],y[i][1],y[i][2]]=img[y[i][0],y[i][1],y[i][2]]+1
    return img
def decode_lsb(img):
    mess="iEzo5vpLzGuAjCzqZpLw74E88GonKYeygxmAbvUjU9MiViKLoD7JtzAVawqELbpmAr9Tftq87nzgUGo5v98YBvG88jJynfpt2epDJZgTWVdctiiHyduVrNieXjjTgNiR"
    binary_string = ''.join(format(ord(char), '08b') for char in mess)
    text=""
    for i in range(0,len(binary_string)): # chỗ này là để lấy độ dài của message cần gửi
        if img[y[i][0],y[i][1],y[i][2]]%2==0:
            text=text+'0'
        if img[y[i][0],y[i][1],y[i][2]]%2==1:
            text=text+'1'
    binary_segments = [text[i:i+8] for i in range(0, len(text), 8)]

# Convert each binary segment to its corresponding character and join them
    result_string = ''.join(chr(int(segment, 2)) for segment in binary_segments)
    return result_string

if __name__ == "__main__":
    #ChaoticsMap(3.57,0.45676)
    img=ReadImage("lena.png")
    PM_c=np.float16(np.average(img))
    print(PM_c)
    Text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam." #thong tin can nen
    Ascii_Values = [ord(char) for char in Text]
    PM_s=np.float16(np.average(Ascii_Values))
    print(PM_s)
    x0=x_k*PM_c-math.floor(x_k*PM_c)
    u0=4*(u*PM_s-math.floor(u*PM_s))
    height, width, _ = img.shape
    s=3*height *width
    ChaoticsMap(u0,x0,s)
    #print(s)
    #print(x)
    sorted_indices = sorted(range(len(x)), key=lambda i: x[i])
    y=embedding_position_matrix(sorted_indices,height,width)
    img=lsb(y,Text,img)
    RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imsave("lena-emb.png", RGB_img)
    img1=ReadImage("lena-emb.png")
    print(decode_lsb(img1))



    