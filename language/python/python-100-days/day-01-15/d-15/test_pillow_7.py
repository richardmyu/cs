'''滤镜效果'''

from PIL import Image, ImageFilter

image = Image.open('./as34w8.jpg')

image.filter(ImageFilter.CONTOUR).show()
