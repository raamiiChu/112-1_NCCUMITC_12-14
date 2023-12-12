import cv2

cap = cv2.VideoCapture(0)

# 載入人臉模型
face_cascade = cv2.CascadeClassifier("./models/haarcascade_frontalface_default.xml")

while True:
    success, img = cap.read()

    if not success:
        break

    # 按下 q 鍵停止
    if cv2.waitKey(1) == ord('q'):
        break

    # 將圖片轉成灰階
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 偵測人臉
    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)   # 標記人臉

    cv2.imshow("face detection", img)

cap.release()
cv2.destroyAllWindows()