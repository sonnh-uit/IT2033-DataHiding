from steganogan import SteganoGAN

dense_steganogan = SteganoGAN.load(architecture='dense')
basic_dense_steganogan = SteganoGAN.load(architecture='basic')

context = {
    "input" : "input/lena.png",
    "output" : "results/output.png",
    "secret_message" : open("input/message.txt").read()
}

def steganogan_encode(context):
    dense_steganogan.encode(context['input'], context['output'], context['secret_message'])

def steganogan_decode(context):
    dense_steganogan.decode(context['output'])


if __name__ == "__main__":
    steganogan_encode(context)
    steganogan_decode(context)
# steganogan.encode('input/lena.png', 'results/output.png', 'This is a super secret message!')

# print(steganogan.decode('results/output.png'))


# sudo docker compose run steganogan steganogan encode lena.png 'this is secret message'