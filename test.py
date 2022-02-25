import os


def get_images(path):
    for filename in os.listdir(path):
        with open(path+'/'+filename, "rb") as f:
            print(f)

def kek():
    print(os.listdir(''))

get_images('./visionLabs/images')