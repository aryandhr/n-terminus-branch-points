import xml.etree.ElementTree as ET
import os
import shutil

from PIL import Image, ImageDraw
from convert import xml_to_yolo

image_dir = "image_data"
xml_dir = "marker_xml_data"
annotated_dir = "annotated_image_data"
yolo_labels = "yolo_labels"
validate_dir = "/Users/aryan/Desktop/branch_data/validate"  # New directory for images without XML files

branch_points = {}

images = [file for file in os.listdir(image_dir)]

for image in images:
    # Construct the corresponding XML file name
    file_name = os.path.splitext(image)[0]
    xml_file_path = os.path.join(xml_dir, "CellCounter_" + file_name + ".xml")
    branch_count = 0

    # Check if the XML file exists for the current TIFF file
    if not os.path.exists(xml_file_path):
        print(f"Skipping {file_name} as no corresponding XML file found.")
        source_image_path = os.path.join(image_dir, image)
        dest_image_path = os.path.join(validate_dir, image)
        os.makedirs(os.path.dirname(dest_image_path), exist_ok=True)
        shutil.move(source_image_path, dest_image_path)
        continue

    # Path to the TIFF image
    tiff_image_path = os.path.join(image_dir, file_name + ".tif")

    # Load the TIFF image
    image = Image.open(tiff_image_path)
    draw = ImageDraw.Draw(image)

    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Iterate through marker data in the XML
    txt_file_path = os.path.join(yolo_labels, file_name + ".txt")
    with open(txt_file_path, 'w') as txt_file:
        # Parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # Iterate through marker data in the XML
        for marker in root.findall(".//Marker"):
            x = int(marker.find("MarkerX").text)
            y = int(marker.find("MarkerY").text)

            # Draw a marker on the image
            draw.ellipse([x - 2, y - 2, x + 2, y + 2], fill="white", outline="red")
            branch_count += 1

            # Convert to YOLO format
            x_yolo, y_yolo = xml_to_yolo(tiff_image_path, x, y)

            # Write the YOLO format coordinates to the txt file
            txt_file.write(f"0 {x_yolo} {y_yolo} 0.009 0.009\n")

    # Save the annotated image with the specified format (e.g., TIFF)
    annotated_image_path = os.path.join(annotated_dir, file_name + ".tif")
    image.save(annotated_image_path, format="TIFF")
    branch_points[file_name] = branch_count

    # Close the TIFF image
    image.close()

print(branch_points)
print("Items: ", len(branch_points), "Total branch instances: ", sum(branch_points.values()))
