import os

from ultralytics import YOLO
from PIL import Image, ImageDraw


model = YOLO("runs/detect/train2/weights/best.pt")

# use absolute path
image = "/Users/aryan/Desktop/branch_data/validate/20x-Delta-N-GM-120HR-L1-N1-A3-Q1-final-SAD113019.tif"

predictions_yolo = "predictions_yolo" # save in new directory so as to not overwrite actual labels received from dataset

results = model(image)  # list of Results objects

for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    #im.save('results.jpg')  # save image
    image_name = os.path.basename(image)
    label_name = os.path.splitext(image_name)[0] + ".txt"
    label_path = os.path.join(predictions_yolo, label_name)
    r.save_txt(label_path) # save predictions in yolo_labels directory under same name
