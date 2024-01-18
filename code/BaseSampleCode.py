import cv2
from cellpose import models

# Load an example image (replace 'your_image.jpg' with the actual image file)
image_path = '/Users/mohammadsadegh/PycharmProjects/cellpose/dataset/lab/original/MM 437 LH C33_m034_eGFP  PV+ ab.png'
img = cv2.imread(image_path)

# Initialize the Cellpose model for nuclei segmentation
model = models.Cellpose(gpu=True, model_type='nuclei')

# Perform segmentation
masks, flows, styles, diams = model.eval(img, diameter=30, channels=[0, 0])

# Save the segmented masks (replace 'output_masks.png' with the desired file name)
cv2.imwrite('output_masks.png', masks[0])

