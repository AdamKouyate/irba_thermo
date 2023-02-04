import cv2
import os

# The path to the folder containing the images
folder_path = './images'

# List all the files in the folder
for filename in os.listdir(folder_path):
    # Construct the full path to the image
    image_path = os.path.join(folder_path, filename)

    # Check if the current file is an image
    if os.path.isfile(image_path) and image_path.endswith(".png"):
        # Read the image
        img = cv2.imread(image_path)

        # Apply a false color map to the image
        img = cv2.applyColorMap(img, cv2.COLORMAP_JET)


        # Resize the image
        img = cv2.resize(img, (480, 480))

        # Display the image
        cv2.imshow(filename, img)

        # Wait until a key is pressed
        cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
