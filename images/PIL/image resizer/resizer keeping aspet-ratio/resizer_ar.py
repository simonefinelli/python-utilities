"""

Resize an image keeping aspect ratio

"""
import PIL
from PIL import Image

max_size = 512

img = Image.open('img1.jpg')

width, height = img.size

if height < max_size and width < max_size:
	img.save('resized.png')
	exit()

if height > width:
	ratio = width / height
	new_width = int(ratio * max_size)
	img = img.resize((new_width, max_size))
else:
	ratio = height / width
	new_height = int(ratio * max_size)
	img = img.resize((max_size, new_height))

img.save('resized.png')