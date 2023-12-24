import io
import tempfile
from PIL import Image
import requests
import face_recognition
import PrintRollnos

PR = PrintRollnos.RollNumbers()
n = int(input("Enter no: "))
year = int(input("Year ( 23 || 22 || 21 || 20 ): "))
Branch = input("Branch ( 01 || 02 || 03 || 04 || 05 || 12 || 66 || 67 ): ")

allRolls = PR.get(n,year,Branch)
count = 0
matches = 0
Matches_rolls = []
known_image = face_recognition.load_image_file("/mnt/c/PROGRAMS/PYTHON/FaceDetec tion/ME_TEST.png")
start = int(input("Start range (from start? enter 0 ) : "))
end = int(input("End range: (to end? enter -1 ) : "))
outCOmes = []
for rollNo in allRolls[start:end]:
    count+=1
    print(count)
    url_1 = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/"
    url_end = "/" + rollNo + ".jpg"
    MainURL = url_1 + rollNo + url_end
    response = requests.get(MainURL)
    if response.status_code == 200:
        file_extension = url_end.split('.')[-1]
        image = Image.open(io.BytesIO(response.content))
        with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{file_extension}') as temp_file:
            image.save(temp_file.name)
        unknown_image = face_recognition.load_image_file(temp_file.name)
        biden_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
        gap = face_recognition.face_distance([biden_encoding], unknown_encoding)
        if(results[0]):
            matches+=1
            print("Found",MainURL)
            print("Roll No: ",rollNo)
            print("Match number: ",matches)
            print('FACE GAP % : ',gap)
            outCOmes.append([rollNo,(100 - (gap*100))])
            print("MATCH : ",100 - (gap*100))
        else:
            continue
            # print("Finding... ",count)
    else:
        print(f"Error: Failed to fetch image, status code {response.status_code}")
print("Total Matches: ",matches)
best = 0
BEST_ROLL = ""
for match in  outCOmes:
    if(match[1][0]>80):
        print("80%%  match: ",match[0])
    if(match[1][0]>best):
        best = match[1][0]
        BEST_ROLL = match[0]
print(f"Best Match : {best} , {BEST_ROLL}")
    
