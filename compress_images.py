"""Compress all images from the project.

REQUIREMENTS:
    - PNGQUANT: sudo apt-get install pngquant
    - PIL: pip install pillow
"""

# coding: utf-8

import os
import glob
from PIL import Image

RED_ALERT = "\033[1;31;49m %s"
GREEN_ALERT = "\033[1;32;49m %s"
ORANGE_ALERT = "\033[1;33;49m %s"
WHITE_ALERT = "\033[1;37;49m %s"

COMPRESS_QUALITY = 70


def find_all_images():
    """Search for all PNG and JPG formats."""
    project_path = os.getcwd()
    print WHITE_ALERT % (
        'Search for all images in the project: %s' % project_path
    )
    all_jpegs = []
    all_pngs = []

    for x in os.walk(project_path):
        for jpg in glob.glob(os.path.join(x[0], '*.jpg')):
            all_jpegs.append(jpg)

        for png in glob.glob(os.path.join(x[0], '*.png')):
            all_pngs.append(png)

    total = len(all_pngs) + len(all_jpegs)
    print GREEN_ALERT % ('TOTAL: %s images found...' % total)
    return [all_pngs, all_jpegs]


def compress_images():
    u"""Compress all imagens found."""
    all_images = find_all_images()
    pngs = all_images[0]
    jpgs = all_images[1]

    print ORANGE_ALERT % 'Compress all PNG files...'
    for p in pngs:
        command = 'pngquant %s --quality 70 --force --output %s' % (p, p)
        os.system(command)

    print GREEN_ALERT % '[DONE]'
    print ORANGE_ALERT % 'Compress all JPG files...'
    for j in jpgs:
        img = Image.open(j)
        img.save(j, format="JPEG", quality=COMPRESS_QUALITY)
    print GREEN_ALERT % '[DONE]'

if __name__ == '__main__':
    print GREEN_ALERT % u'[Start Project Image Compression ]...'
    try:
        compress_images()
    except Exception as err:
        print RED_ALERT % u'[Ops! we got an error. please checkout your branch (If possible)]'
    print GREEN_ALERT % u'[Script Ended]'
