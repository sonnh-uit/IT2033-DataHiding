
### Test
- Base on the task strcutre, I ease to put some test to `variables.yml`. I have 6 cases with 2 pictures. Two picture are two size
    - The `lena.png` is most popular example. It has 512x512 pixel
    - The `babylon.png` is lesser, but still popular. It has 2012x1482
- The secret I use was generate by [Lorem Ipsum](https://www.lipsum.com/) with 3 size: 50 bytes, 500 bytes and 5000 bytes (corresponding small, large and extra in my definition)
- After testing:
    - In LSB, it cannot hiding more text. The extra message can embeded with no error but cannot take back. The pictures after encode are similar before.
    - In DCT, it cannot hiding extra text, it have error when I embed. But the text with success embed ensure take back in decode process. The picture after hiding not look same before and difference the resule of decode process.  