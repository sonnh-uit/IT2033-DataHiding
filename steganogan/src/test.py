from steganogan import SteganoGAN
steganogan = SteganoGAN.load(architecture='dense')

# steganogan.encode('input/lena.png', 'results/output.png', 'This is a super secret message!')

# print(steganogan.decode('results/output.png'))
steganogan.decode('results/output.png')

# sudo docker compose run steganogan steganogan encode lena.png 'this is secret message'