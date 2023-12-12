import cv2

# 開啟圖片
img = cv2.imread("./images/kekw.jpg")  # cv2.IMREAD_COLOR (BGR)

# 加強
# 增加細節和清晰度
enhance = img
alpha = 2
beta = 10
cv2.convertScaleAbs(img, enhance, alpha, beta)  # 公式：output = img*alpha + beta

cv2.imshow("The Image", enhance)  # 使用視窗開啟圖片
cv2.waitKey(0)                # 按下任意鍵停止
cv2.destroyAllWindows()       # 結束所有圖片視窗