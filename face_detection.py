
import cv2
import matplotlib.pyplot as plt

# Image and model paths
imagePath = "image.png"
cascPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

# Load Haar Cascade classifier
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)

if image is None:
    print("Image not found! Check image.png")
    exit()

if faceCascade.empty():
    print("Haar Cascade model not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

print("Found", len(faces), "faces!")

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y),
                  (x+w, y+h), (0, 255, 0), 2)

# Save output
cv2.imwrite("output.png", image)

# Display output
RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)
plt.axis("off")
plt.show()
