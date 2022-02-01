from PIL import Image
import numpy as np

def img_to_array(img):    
    R, G, B = 0, 1, 2
    X, Y = 0, 1

    pixel = img.load()

    R_mat = []
    G_mat = []
    B_mat = []
    for row in range(img.size[X]):
        row_R = []
        row_G = []
        row_B = []
        for col in range(img.size[Y]):
            row_R.append(pixel[row, col][R])
            row_G.append(pixel[row, col][G])
            row_B.append(pixel[row, col][B])
        R_mat.append(row_R)
        G_mat.append(row_G)
        B_mat.append(row_B)
    pix_arr = [np.array(R_mat), np.array(G_mat), np.array(B_mat)]
    return pix_arr

def array_to_img(pix_arr):

    return img

# Main Script
R, G, B = 0, 1, 2

file_name = 'test.png'
img = Image.open('Imports\\' + file_name)

pix_arr = img_to_array(img) # [R_mat, G_mat, B_mat]

print(pix_arr)
print(np.linalg.eigvals(np.matmul(np.transpose(pix_arr[R]), pix_arr[R])))



img.save('Exports\\' + file_name)
