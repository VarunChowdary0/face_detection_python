import face_recognition

# Load known images with faces
print("Training your face")
known_image_paths = ["./MyFaces/f1.jpg","./MyFaces/f3.jpg",
                     "./MyFaces/f4.jpg","./MyFaces/Me2.png",
                     "./MyFaces/MyFace.png","./MyFaces/meChildhood.png",
                     "./MyFaces/mypic1.png","./MyFaces/mypic.jpg"]

known_face_encodings = []

for image_path in known_image_paths:
    known_image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(known_image)[0]  # Assuming there is only one face in each image
    known_face_encodings.append(face_encoding)

print("Training Complete")
# Load an unknown image with a face to compare
unknown_image_path = "vamshi.png"
unknown_image = face_recognition.load_image_file(unknown_image_path)
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare the unknown face encoding with each known face encoding
results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)
gap = face_recognition.face_distance(known_face_encodings,unknown_face_encoding)
sum = 0
for i, result in enumerate(results):
    sum+=100-(gap[i]*100)
    if result and 100-(gap[i]*100)>(55):
        print(f"The unknown face matches with person {i+1} Accuraccy - {100-(gap[i]*100)}")
    else:
        print(f"The unknown face does not match with person {i+1} accuraccy - {100-(gap[i]*100)}")
print(sum/len(gap))