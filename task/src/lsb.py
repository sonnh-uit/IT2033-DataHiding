from PIL import Image
class LSB():
    def encode_image(self,imgage, msg):
        length = len(msg)
        encode_pic = imgage.copy()
        width, height = imgage.size
        index = 0
        for row in range(height):
            for col in range(width):
                if imgage.mode != 'RGB':
                    r, g, b ,a = imgage.getpixel((col, row))
                elif imgage.mode == 'RGB':
                    r, g, b = imgage.getpixel((col, row))
                if row == 0 and col == 0 and index < length:
                    asc = length
                elif index <= length:
                    c = msg[index -1]
                    asc = ord(c)
                else:
                    asc = b
                encode_pic.putpixel((col, row), (r, g , asc))
                index += 1
        return encode_pic

    def decode_image(self,imgage):
        width, height = imgage.size
        msg = ""
        index = 0
        for row in range(height):
            for col in range(width):
                if imgage.mode != 'RGB':
                    r, g, b, a = imgage.getpixel((col, row))
                elif imgage.mode == 'RGB':
                    r, g, b = imgage.getpixel((col, row))

                if row == 0 and col == 0:
                    length = b
                    continue  

                if index < length:
                    msg += chr(b)
                else:
                    break 
                index += 1

        original_img = Image.new(imgage.mode, imgage.size)
        index = 0
        for row in range(height):
            for col in range(width):
                r, g, b = imgage.getpixel((col, row))  

                if row == 0 and col == 0:
                    original_img.putpixel((col, row), (r, g, length))
                else:
                    if index < len(msg):
                        original_img.putpixel((col, row), (r, g, ord(msg[index])))
                        index += 1
                    else:
                        original_img.putpixel((col, row), (r, g, b)) 
       
        return original_img, msg