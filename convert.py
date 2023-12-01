from PIL import Image


def xml_to_yolo(image, x, y):
    with Image.open(image) as img:
        width, height = img.size

    x1, y1 = x / width, y / height
    return x1, y1
