from steganogan import SteganoGAN

dense_steganogan = SteganoGAN.load(architecture='dense')
basic_dense_steganogan = SteganoGAN.load(architecture='basic')

test_cases = [
    {
        "input": "input/lena.png",
        "output": "results/output1.png",
        "secret_message": open("input/message1.txt").read()
    },
    {
        "input": "input/landscape.jpg",
        "output": "results/output2.png",
        "secret_message": open("input/message2.txt").read()
    },
    {
        "input": "input/beach.png",
        "output": "results/output3.png",
        "secret_message": open("input/message3.txt").read()
    },
    {
        "input": "input/city.jpg",
        "output": "results/output4.png",
        "secret_message": open("input/message4.txt").read()
    },
    {
        "input": "input/mountain.png",
        "output": "results/output5.png",
        "secret_message": open("input/message5.txt").read()
    },
    {
        "input": "input/forest.jpg",
        "output": "results/output6.png",
        "secret_message": open("input/message6.txt").read()
    },
    {
        "input": "input/river.png",
        "output": "results/output7.png",
        "secret_message": open("input/message7.txt").read()
    },
    {
        "input": "input/sunset.jpg",
        "output": "results/output8.png",
        "secret_message": open("input/message8.txt").read()
    },
    {
        "input": "input/sky.png",
        "output": "results/output9.png",
        "secret_message": open("input/message9.txt").read()
    },
    {
        "input": "input/field.jpg",
        "output": "results/output10.png",
        "secret_message": open("input/message10.txt").read()
    },
]

def steganogan_encode(context):
    dense_steganogan.encode(context['input'], context['output'], context['secret_message'])

def steganogan_decode(context):
    dense_steganogan.decode(context['output'])

if __name__ == "__main__":
    for test_case in test_cases:
        steganogan_encode(test_case)
        steganogan_decode(test_case)
