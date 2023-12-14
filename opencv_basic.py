# pip install opencv-python
import cv2

# 開啟圖片
img = cv2.imread("./images/kekw.jpg")  # cv2.IMREAD_COLOR (BGR)
# img = cv2.imread("./images/kekw.jpg", cv2.IMREAD_GRAYSCALE)  # cv2.IMREAD_GRAYSCALE (灰階)

print(img)
print(f"width:  {len(img)}") 
print(f"height: {len(img[0])}")

# cv2.imwrite("./images/new_kekw.jpg", img)  # 儲存圖片

cv2.imshow("The Image", img)  # 使用視窗開啟圖片
cv2.waitKey(0)                # 按下任意鍵停止
cv2.destroyAllWindows()       # 結束所有圖片視窗