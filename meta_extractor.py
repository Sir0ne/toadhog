from PIL import Image
from PIL.ExifTags import TAGS
from glob import glob
import json


imgfiles = []
for file in glob("*.jpg"):
    imgfiles.append(file)

# Sort through all images available
for n in range(len(imgfiles)):
    current_img = imgfiles[n]
    current_img = current_img.replace('.JPG', '')
    image = Image.open(f"{current_img}.jpg")
    exif_data = image.getexif()
    pull_tags = ['Model', 'DateTime']   

    # Extracts tags from pictures
    exif_table = {}
    for k in exif_data:
        tag = TAGS.get(k, k)
        v = exif_data.get(k)
        
        # Convert raw to utf-8
        if isinstance(v, bytes):
            try:
                v.decode("utf-8", errors="ignore")
            except:
                v = str(v)
        
        # Sanitise UTF-8     
        if isinstance(v, str):
            v = v.replace('\x00', '')
        exif_table[tag] = v

    # Outputs extracted tags to JSON file
    with open(f'META{current_img}.json', 'w') as file:
        json.dump(exif_table, file, indent=4, default=str, ensure_ascii = False)
