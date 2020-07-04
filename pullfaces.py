from PIL import Image
import face_recognition



image=face_recognition.load_image_file('./img/groups/team1.jpg')
face_locations=face_recognition.face_locations(image)

for face_location in face_locations:
    top,right,bottom,left=face_location

    face_image=image[top:bottom,left:right]
    pill_image=Image.fromarray(face_image)
    # pill_image.show()
    pill_image.save(f'{top}.jpg')