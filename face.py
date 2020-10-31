import face_recognition
import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()


a1 = face_recognition.load_image_file('a1.jpg')
a1_encoding = face_recognition.face_encodings(a1)[0]

a6 = face_recognition.load_image_file('./opencv_frame_0.png')
#face_locations = face_recognition.face_locations(a6)
a6_encoding = face_recognition.face_encodings(a6)[0]


# Compare faces
result1 = face_recognition.compare_faces([a1_encoding], a6_encoding)
v=0
print("\n\n\n\n")
for i in result1:
    if i:
        print('This is you')
        v=v+1

if v==0:
    print('This is NOT you')


