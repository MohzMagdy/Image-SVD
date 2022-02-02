from PIL import Image
from image_matrix import *

# Main Script
file_name = 'test.png'
img = Image.open('Imports\\' + file_name)

pix_arr = img_to_array(img) # [R_mat, G_mat, B_mat]


# Test code
for row in range(img.size[0]):
    for col in range(img.size[1]):
        pix_arr[R][row, col] = 0


img = array_to_img(img, pix_arr)
img.save('Exports\\' + file_name)