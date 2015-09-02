# -*- coding: utf-8 -*-
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def main():
    get_type ="DateTimeOriginal"
    exif_data = []
    im = Image.open("test.jpg")
    exif = im._getexif()

    for id, value in exif.items():
        if TAGS.get(id) == get_type:
            tag = TAGS.get(id, id),value
            exif_data.extend(tag)

    print exif_data

if __name__ == "__main__":
    main()
