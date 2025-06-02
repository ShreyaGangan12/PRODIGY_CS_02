from PIL import Image
import numpy as np

print("Welcome to Image Cryptor!!!\nOptions:\n1. Encrypt\t2. Exit")
print("\n**Encryption of an image twice causes decryption producing the original image**\n")

def crypt():
    path = input('Enter path of Image: ').strip('"')
    try:
        print('Enter sequence of 3 integers (0 < key < 256) for encryption of Image:')
        key = np.array([np.uint8(input()), np.uint8(input()), np.uint8(input())])
        if not all(0 < x < 256 for x in key):
            print("Invalid key values. Please enter integers in the range 0 to 255.")
            return
        img = Image.open(path)
        img_array = np.array(img)
        key = np.resize(key, img_array.shape)
        encrypted_array = np.bitwise_xor(img_array, key)
        encrypted_img = Image.fromarray(encrypted_array)
        encrypted_img.save("crypted_image.png")
        print("Image encrypted successfully.")
    except FileNotFoundError:
        print("File not found. Please enter a valid path.")

while (True):
    opt=int(input("Enter option: "))
    if opt==1:
        crypt()
    elif opt==2:
        print("Thankyou!!")
        break
    else:
        print("Invalid Option!")
