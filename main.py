from PIL import Image
from image_matrix import *
from manualTruncatingSVD import *
import os
import sys

# Main Script
path = sys.path[0] + '\\Imports'
while True:
    print(os.listdir(path))
    file_name = input('Enter file name: ')
    try:
        img = Image.open('Imports\\' + file_name)
        break
    except:
        print('Invalid file name')

# Check dimensions
is_resized = False
if img.size[X] == img.size[Y]:
    img = img.resize((img.size[X], img.size[Y] + 1))
    is_resized = True

pix_arr = img_to_array(img) # [R_mat, G_mat, B_mat]

is_transposed = False
if img.size[X] < img.size[Y]:
    for i in range(len(pix_arr)):
        pix_arr[i] = np.transpose(pix_arr[i])
    is_transposed = True


# SVD on image
for i in range(len(pix_arr)):
    mat = mtsvd(pix_arr[i])
    pix_arr[i] = mat[0] @ mat[1] @ np.transpose(mat[2])


# Reset image dimensions
if is_transposed:
    for i in range(len(pix_arr)):
        pix_arr[i] = np.transpose(pix_arr[i])
if is_resized:
    img = img.resize((img.size[X], img.size[Y] - 1))

img = array_to_img(img, pix_arr)
img.save('Exports\\' + file_name, format='jpeg')
print('Compression Complete!')