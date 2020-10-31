import cv2


cap = cv2.VideoCapture('out1.mp4')
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

out = cv2.VideoWriter("output.mp4", fourcc, 5.0, (1280, 720))
alert = cv2.VideoWriter("alert.mp4", fourcc, 5.0, (1280, 720))
alertv = 0

ret, frame1 = cap.read()
ret, frame2 = cap.read()
print(frame1.shape)
num = 0
num1 = 0
while cap.isOpened():
    num1 += 1
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 1200:
            image = cv2.resize(frame1, (1280, 720))
            alertv = 1
            # print("\n\n change \n\n")
            continue

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    if (alertv == 1):
        alert.write(image)
        alertv = 0
        num = num + 1
    image = cv2.resize(frame1, (1280, 720))
    out.write(image)
    cv2.imshow("Feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if (ret == False):
        break

    if cv2.waitKey(40) == 27:
        break

# print(num)
# print(num1)

if (num1 - num > 10):
    print("Wipers are not working")
else:
    print("Wipers are working well")

cv2.destroyAllWindows()
cap.release()
out.release()
alert.release()

