from PIL import Image
from PIL.ExifTags import TAGS

imagename = "66138481-9ebf-41d7-a068-0775e88a8e26.jpg"

image = Image.open(imagename)

info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Format": image.format
}

for label,value in info_dict.items():
    print(f"{label:25}: {value}")
    
 exifdata = image.getexif()
 
 for tag_id in exifdata:
     tag = TAGS.get(tag_id, tag_id)
     data = exifdata.get(tag_id)