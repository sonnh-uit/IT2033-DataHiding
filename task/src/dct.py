import numpy as np
import cv2
import itertools
from PIL import Image


quant = np.array([[16,11,10,16,24,40,51,61],      
                    [12,12,14,19,26,58,60,55],   
                    [14,13,16,24,40,57,69,56],
                    [14,17,22,29,51,87,80,62],
                    [18,22,37,56,68,109,103,77],
                    [24,35,55,64,81,104,113,92],
                    [49,64,78,87,103,121,120,101],
                    [72,92,95,98,112,100,103,99]])

class DCT():    
    def __init__(self): 
        self.message = None
        self.bitMess = None
        self.oriCol = 0
        self.oriRow = 0
        self.numBits = 0   

    def chunks(self, l, n):
        m = int(n)
        for i in range(0, len(l), m):
            yield l[i:i + m]
    def addPadd(self,img, row, col):
        img = cv2.resize(img,(col+(8-col%8),row+(8-row%8)))    
        return img
    def toBits(self):
        bits = []
        for char in self.message:
            binval = bin(ord(char))[2:].rjust(8,'0')
            bits.append(binval)
        self.numBits = bin(len(bits))[2:].rjust(8,'0')
        return bits

    def encode_image(self,img,secret_message):

        secret=secret_message
        self.message = str(len(secret))+'*'+secret
        self.bitMess = self.toBits()
        row,col = img.shape[:2]
        self.oriRow, self.oriCol = row, col  
        if((col/8)*(row/8)<len(secret)):
            print("Error: Message too long to encode in image")
            return False
 
        if row%8 != 0 or col%8 != 0:
            img = self.addPadd(img, row, col)
        
        row,col = img.shape[:2]
        bImg,gImg,rImg = cv2.split(img)
        bImg = np.float32(bImg)
        imgBlocks = []
        for (j,i) in itertools.product(range(0,row,8),range(0,col,8)):
            block = bImg[j:j+8, i:i+8]
            block -= 128
            block = np.round(block)
            imgBlocks.append(block)
        dctBlocks = []
        for img_Block in imgBlocks:
            dct_block = np.round(cv2.dct(img_Block))
            dctBlocks.append(dct_block)
        quantizedDCT = []
        for dct_Block in dctBlocks:
            quantized_block = np.round(dct_Block / quant)
            quantizedDCT.append(quantized_block)
        
        messIndex = 0
        letterIndex = 0
        for quantizedBlock in quantizedDCT:
            DC = quantizedBlock[0][0]
            DC = np.uint8(DC)
            DC = np.unpackbits(DC)
            DC[7] = self.bitMess[messIndex][letterIndex]
            DC = np.packbits(DC)
            DC = np.float32(DC)
            DC= DC-255
            quantizedBlock[0][0] = DC
            letterIndex = letterIndex+1
            if letterIndex == 8:
                letterIndex = 0
                messIndex = messIndex + 1
                if messIndex == len(self.message):
                    break
        sImgBlocks = [quantizedBlock *quant+128 for quantizedBlock in quantizedDCT]
        sImg=[]
        for chunkRowBlocks in self.chunks(sImgBlocks, col/8):
            for rowBlockNum in range(8):
                for block in chunkRowBlocks:
                    sImg.extend(block[rowBlockNum])
        sImg = np.array(sImg).reshape(row, col)
        sImg = np.uint8(sImg)
        sImg = cv2.merge((sImg,gImg,rImg))
        return sImg
    

    def decode_image(self,img):
        row,col = img.shape[:2]
        messSize = None
        messageBits = []
        buff = 0
        try:
            bImg, gImg, rImg = cv2.split(img)
        except ValueError as e:
            return Image.fromarray(img), str(e)
        bImg = np.float32(bImg)

        imgBlocks = []
        for (j, i) in itertools.product(range(0, row, 8), range(0, col, 8)):
            block = bImg[j:j+8, i:i+8]
            block -= 128
            imgBlocks.append(block)
        # imgBlocks = [bImg[j:j+8, i:i+8]-128 for (j,i) in itertools.product(range(0,row,8),range(0,col,8))]
        quantizedDCT = []
        for img_Block in imgBlocks:
            # quantized_block = img_Block / quant
            quantized_block = img_Block / np.resize(quant, img_Block.shape)            
            quantizedDCT.append(quantized_block)
        # quantizedDCT = [img_Block/quant for img_Block in imgBlocks]
        i=0
        for quantizedBlock in quantizedDCT:
            DC = quantizedBlock[0][0]
            DC = np.uint8(DC)
            DC = np.unpackbits(DC)
            if DC[7] == 1:
                buff+=(0 & 1) << (7-i)
            elif DC[7] == 0:
                buff+=(1&1) << (7-i)
            i=1+i
            if i == 8:
                messageBits.append(chr(buff))
                buff = 0
                i =0
                if messageBits[-1] == '*' and messSize is None:
                    try:
                        messSize = int(''.join(messageBits[:-1]))
                    except:
                        pass
            if len(messageBits) - len(str(messSize)) - 1 == messSize:
                break
        sImgBlocks = [quantizedBlock *quant+128 for quantizedBlock in quantizedDCT]
        sImgBlocks = [cv2.idct(B)+128 for B in quantizedDCT]
        sImg=[]
        for chunkRowBlocks in self.chunks(sImgBlocks, col // 8):
            for rowBlockNum in range(8):
                for block in chunkRowBlocks:
                    sImg.extend(block[rowBlockNum])
        sImg = np.array(sImg).reshape(row, col)
        sImg = np.uint8(sImg)
        sImg = cv2.merge((sImg,gImg,rImg))
        message = ''.join(messageBits)[len(str(messSize))+1:]
        sImg_pil = Image.fromarray(sImg)
        return sImg_pil, message


    
  