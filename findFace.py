import face_recognition

image=face_recognition.load_image_file('./img/groups/team1.jpg')

face_location=face_recognition.face_locations(image)
print(face_location)
TotalPeople=len(face_location)
print(f'There Are  people {TotalPeople} in this image')