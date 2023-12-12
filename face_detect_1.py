# OpenCV 官方資料集 Github
# https://github.com/opencv/opencv/tree/4.x/data
import cv2

# 載入圖片
img = cv2.imread("./images/singer1.jpg")

# 將圖片轉成灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 載入人臉模型
face_cascade = cv2.CascadeClassifier("./models/haarcascade_frontalface_default.xml")

# 偵測人臉
faces = face_cascade.detectMultiScale(gray)

# 為每個人臉繪製方框
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("face detection", img)
cv2.waitKey(0) # 按下任意鍵停止
cv2.destroyAllWindows()