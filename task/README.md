# Week 2 & week 3 task



- Student UID: 220202022
- Fullname: Nguyen Hong Son

## Intruduce
### Task introduce
- This task has build with docker. To run this task, just [install docker](https://docs.docker.com/engine/install/ubuntu/) and run the following command
    ```
    sudo docker compose up
    ```
- When running, docker will create environment which seting in [Dockerfile](Dockerfile). If you want to run this task without docker, note that you has had install all package mention in `Dockerfile`.
- `src` foler containt all source of this task, it write by python and has:
    - The [origin_imgs](src/origin_imgs/) folder. There are two picture I use for tesing in my task.
    - [dct.py](src/dct.py) and [lsb.py](src/lsb.py) are two file have a class can process LSB and DCT algorthim.
    - [main.py](src/main.py) is main file of this task. It running with read input parameter from [variables.yaml](src/variables.yaml) and start hidding, encoding the secret to/from the picture. Then, create two folder, one for save encoded result, one for decoded result.

### For my algorithm
I just use very easy algorith for both LSB and DCT.
#### LSB
- For encode, I loop in two side of picture. Save length of message for first pixel. I hide each character to blue chanel of picture.
- For decode, I revert the encode process and get secret message. Return the message and the origin picture.

#### DCT
- For encode, I performs DCT on 8x8 blocks of the blue channel of the image, quantizes the coefficients using the quant matrix, and embeds the secret message into the DC (Direct Current) coefficient of each block.
- For decode, I take embed image, decodes the secret message embedded in the image using the same quantization process used during encoding. Then I extracts the message bits from the DC coefficients of the DCT blocks.

#### Evaluate
- My algorithm is very simple. It not have chaotic map, key or other method can extend security or robustness.
- My algorithm easy to decode, not secucity, not robustness, and less performance embeded secret message.

### Test
- Base on the task strcutre, I ease to put some test to `variables.yml`. I have 6 cases with 2 pictures. Two picture are two size
    - The `lena.png` is most popular example. It has 512x512 pixel
    - The `babylon.png` is lesser, but still popular. It has 2012x1482
- The secret I use was generate by [Lorem Ipsum](https://www.lipsum.com/) with 3 size: 50 bytes, 500 bytes and 5000 bytes (corresponding small, large and extra in my definition)
- After testing:
    - In LSB, it cannot hiding more text. The extra message can embeded with no error but cannot take back. The pictures after encode are similar before.
    - In DCT, it cannot hiding extra text, it have error when I embed. But the text with success embed ensure take back in decode process. The picture after hiding not look same before and difference the resule of decode process.  