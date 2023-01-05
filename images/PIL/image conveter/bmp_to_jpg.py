import glob
import pathlib
from PIL import Image

if __name__ == "__main__":
    imgs_path = glob.glob("images/*")
    img_extension = '.jpg'

    for img_path in imgs_path:
        img = Image.open(img_path).convert('RGB')
        img_name = pathlib.PurePath(img_path).name + img_extension
        img.save('./converted_images/' + img_name, 'png')