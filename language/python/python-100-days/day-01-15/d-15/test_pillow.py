from PIL import Image

image = Image.open('./23adf9.jpg')

print(f'image.format: {image.format}')
print(f'image.size: {image.size}')
print(f'image.mode: {image.mode}')

image.show()
