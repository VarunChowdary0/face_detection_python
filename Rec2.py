import face_recognition
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Load an image with faces
image_path = "mypic.jpg"
image = face_recognition.load_image_file(image_path)

# Find all face locations in the image
face_locations = face_recognition.face_locations(image)

# Display the image with face rectangles
plt.imshow(image)
for face_location in face_locations:
    top, right, bottom, left = face_location
    rect = patches.Rectangle((left, top), right - left, bottom - top, linewidth=2, edgecolor='r', facecolor='none')
    plt.gca().add_patch(rect)

plt.show()
