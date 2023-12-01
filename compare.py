import os
import shutil

image_dir = "image_data"
annotated_dir = "annotated_image_data"
yolo_labels = "yolo_labels"
images = "images"
labels = "labels"

files1 = [file for file in os.listdir(annotated_dir)]
files2 = [file for file in os.listdir(yolo_labels)]

test1 = set(file[10:-4] for file in files1)
test2 = set(file[:-4] for file in files2)

intersection = list(test1.intersection(test2))

for filename in intersection:
    # Copy the corresponding .tif file to the images directory
    image_file = f"{filename}.tif"
    source_image_path = os.path.join(image_dir, image_file)
    dest_image_path = os.path.join(images, image_file)
    shutil.copy(source_image_path, dest_image_path)

    # Copy the corresponding .txt file to the labels directory
    label_file = f"{filename}.txt"
    source_label_path = os.path.join(yolo_labels, label_file)
    dest_label_path = os.path.join(labels, label_file)
    shutil.copy(source_label_path, dest_label_path)
