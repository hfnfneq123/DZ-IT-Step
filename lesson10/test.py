import cv2
from PIL import Image

# Path to the image and Haar Cascade XML
image_path = 'img_1.png'  # Updated image name
haarcascade_path = 'haarcascade_frontalface_default.xml'  # Updated Haar cascade name

# Load the Haar Cascade for cat faces
cat_face = cv2.CascadeClassifier(haarcascade_path)
if cat_face.empty():
    print("Error: Could not load Haar Cascade file")
    exit()

# Read the input image
image = cv2.imread(image_path)
if image is None:
    print("Error: Could not read image")
    exit()

# Convert image to grayscale for face detection
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect cat faces in the image
cat_faces = cat_face.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

# Debugging: Check if faces are detected
print(f"Detected {len(cat_faces)} cat faces.")
if len(cat_faces) == 0:
    print("No cat faces detected.")
else:
    print(f"Detected {len(cat_faces)} cat faces.")

# Load the glasses image
glasses = Image.open('glasses.png').convert("RGBA")

# Open the original image with PIL
cat = Image.open(image_path).convert("RGBA")

# Debugging: Draw a rectangle around detected faces
for (x, y, w, h) in cat_faces:
    # Draw a rectangle on the image to show the detected face (for debugging)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show the image with rectangles drawn (to check face detection)
cv2.imshow("Detected Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Iterate over detected cat faces and paste glasses on them
for (x, y, w, h) in cat_faces:
    # Resize glasses to fit the face width
    glasses_resized = glasses.resize((w, h // 3))

    # Calculate position to paste glasses on the face
    glasses_position = (x, y + h // 4)

    # Paste the resized glasses image onto the cat image using the alpha channel as mask
    cat.paste(glasses_resized, glasses_position, glasses_resized)

# Save and display the resulting image
output_path = "cat_with_glasses.png"
cat.save(output_path)

# Show the result using OpenCV (optional, but needs to be in BGR format)
cat_new = cv2.imread(output_path)
cv2.imshow("Cat with Glasses", cat_new)
cv2.waitKey(0)
cv2.destroyAllWindows()


