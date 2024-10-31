import cv2
cap = cv2.VideoCapture(0)
list_example = [0, 1, 2 ,3]
sq_len = 100
while True:
    ret, frame = cap.read()
    print(frame.shape)
    height, width, _ = frame.shape
    frame[height - sq_len:, width - sq_len:] = [0, 0, 0]
    frame[:sq_len, :sq_len] = [0, 0, 0]
    frame[:sq_len, width - sq_len:] = [0, 0, 0]
    frame[height - sq_len:, :sq_len] = [0, 0, 0]
    frame[height // 2 - sq_len // 2: height // 2 + sq_len // 2, width // 2 - sq_len // 2: width // 2 + sq_len // 2] = [0, 0, 0]


    cv2.imshow("Албанский компьютерный вирус", frame)
    key = cv2.waitKey(1)
    if key == ord("8"):
        break
cv2.destroyAllWindows()
