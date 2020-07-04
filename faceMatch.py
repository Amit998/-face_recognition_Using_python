import face_recognition

image_of_bill=face_recognition.load_image_file('./img/known/Bill Gates.jpg')
bill_face_encoding=face_recognition.face_encodings(image_of_bill)[0]
# print(bill_face_encoding)

unknown_image=face_recognition.load_image_file('./img/unknown/jordan-basketball.jpeg')
unknown_face_encoding=face_recognition.face_encodings(unknown_image)[0]

result=face_recognition.compare_faces([bill_face_encoding],unknown_face_encoding)
if result[0]:
    print('This is Bill Gates')
else:
    print('This Is Not Bill gates')