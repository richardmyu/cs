'''生成缩略图'''

from PIL import Image

image = Image.open('./23adf9.jpg')

size = 128, 128
image.thumbnail(size)

image.show()
