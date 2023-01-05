# importing Image class from PIL package 
from PIL import Image
   
# creating a object 
image = Image.open('cat.jpg')
# MAX_SIZE = (512, 512)
  
# image.thumbnail(MAX_SIZE)

def resize_image_padded(im, new_size=1024, fill_color=(0, 0, 0, 255)):
    x, y = im.size
    size = max(x, y)
    new_img = Image.new('RGBA', (size, size), fill_color)
    new_img.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    new_img = new_img.resize((new_size, new_size))
    return new_img
  
# creating thumbnail
image = resize_image_padded(image, new_size=224, fill_color=(255, 255, 255, 255))
image.save('pythonthumb.png')
image.show()