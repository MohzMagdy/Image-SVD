from PIL import Image

R, G, B = 0, 1, 2
X, Y = 0, 1

file_name = 'test.png'
img = Image.open('Imports\\' + file_name)

pixel = img.load()

for row in range(img.size[X]):
    for col in range(img.size[Y]):
        pixel[row, col] = (0, pixel[row, col][G], pixel[row, col][B])

img.save('Exports\\' + file_name)

