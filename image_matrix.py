from PIL import Image
import numpy as np

global R, G, B, X, Y
R, G, B, X, Y = 0, 1, 2, 0, 1

def img_to_array(img): 

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

def array_to_img(img, pix_arr):

    pixel = img.load()
    
    for col in range(img.size[Y]):
        for row in range(img.size[X]):
            R_val = int(pix_arr[R][row, col])
            G_val = int(pix_arr[G][row, col])
            B_val = int(pix_arr[B][row, col])

            pixel[row, col] = (R_val, G_val, B_val)
    return img