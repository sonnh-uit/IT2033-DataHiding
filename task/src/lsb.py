from PIL import Image
class LSB():
    #encoding part :
    def encode_image(self,img, msg):
        # length = len(msg)
        # if length > 255:
        #     print("text too long! (don't exeed 255 characters)")
        #     return False
        encoded = img.copy()
        width, height = img.size
        index = 0
        for row in range(height):
            for col in range(width):
                if img.mode != 'RGB':
                    r, g, b ,a = img.getpixel((col, row))
                elif img.mode == 'RGB':
                    r, g, b = img.getpixel((col, row))
                # first value is length of msg
                if row == 0 and col == 0 and index < length:
                    asc = length
                elif index <= length:
                    c = msg[index -1]
                    asc = ord(c)
                else:
                    asc = b
                encoded.putpixel((col, row), (r, g , asc))
                index += 1
        return encoded

    #decoding part :
    def decode_image(self,img):
        width, height = img.size
        msg = ""
        index = 0
        for row in range(height):
            for col in range(width):
                if img.mode != 'RGB':
                    r, g, b, a = img.getpixel((col, row))
                elif img.mode == 'RGB':
                    r, g, b = img.getpixel((col, row))

                if row == 0 and col == 0:
                    length = b
                    continue  # Bỏ qua pixel đầu tiên chứa độ dài

                if index < length:
                    msg += chr(b)
                else:
                    break  # Dừng khi đã đọc đủ độ dài của thông điệp
                index += 1

        original_img = Image.new(img.mode, img.size)
        index = 0
        for row in range(height):
            for col in range(width):
                r, g, b = img.getpixel((col, row))  # Sử dụng kênh màu RGB

                if row == 0 and col == 0:
                    original_img.putpixel((col, row), (r, g, length))
                else:
                    # Kiểm tra xem đã đọc hết thông điệp chưa
                    if index < len(msg):
                        original_img.putpixel((col, row), (r, g, ord(msg[index])))
                        index += 1
                    else:
                        original_img.putpixel((col, row), (r, g, b))  # Sử dụng lại giá trị kênh màu xanh
       
        return original_img, msg