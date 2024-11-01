import cv2
cap = cv2.VideoCapture(0)

while True:
    print(type(cap))
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("Albanian malware", frame)
    key = cv2.waitKey(1)
    if key == ord("8"):
        break
cv2.destroyAllWindows()