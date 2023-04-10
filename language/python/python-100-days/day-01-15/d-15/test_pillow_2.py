'''剪裁图像'''

from PIL import Image

image = Image.open('./23adf9.jpg')
rect = 250, 250, 1361, 1361
image.crop(rect).show()

# image.show()
