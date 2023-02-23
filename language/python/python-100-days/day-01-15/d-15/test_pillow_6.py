'''操作像素'''

from PIL import Image

image = Image.open('./as34w8.jpg')

for x in range(50, 300):
    for y in range(50, 300):
        image.putpixel((x, y), (128, 128, 128))

image.show()
