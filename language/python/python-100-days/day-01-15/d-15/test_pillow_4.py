'''缩放和黏贴图像'''

from PIL import Image

image1 = Image.open('./23adf9.jpg')
image2 = Image.open('./as34w8.jpg')

rect = 250, 250, 500, 500
image2_head = image2.crop(rect)
width, height = image2_head.size
image1.paste(image2_head.resize((int(width), int(height))), (60, 60))
image1.show()
