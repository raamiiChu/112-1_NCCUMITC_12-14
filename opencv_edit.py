import cv2

# 開啟圖片
img = cv2.imread("./images/kekw.jpg")  # cv2.IMREAD_COLOR (BGR)

# 翻轉
flip_0 = cv2.flip(img, 0)    # 上下翻轉
flip_1 = cv2.flip(img, 1)    # 左右翻轉
flip_2 = cv2.flip(img, -1)   # 上下左右翻轉

# 拉伸
resize_0 = cv2.resize(img, (200, 200))
resize_1 = cv2.resize(img, (100, 300))

# 旋轉
rotate_0 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)         # 順時針旋轉 90 度
rotate_1 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)  # 逆時針旋轉 90 度
rotate_2 = cv2.rotate(img, cv2.ROTATE_180)                  # 旋轉 180 度

# 以某點為中心，旋轉指定角度
w, h = (len(img[0]), len(img))  # 取得圖片尺寸
matrix = cv2.getRotationMatrix2D((w/2, h/2), 45, 1)  # 以正中央為圓心旋轉 45 度，尺寸 1
rotate_3 = cv2.warpAffine(img, matrix, (w, h))       # 產生旋轉的影像

cv2.imshow("The Image", rotate_3)  # 使用視窗開啟圖片
cv2.waitKey(0)                # 按下任意鍵停止
cv2.destroyAllWindows()       # 結束所有圖片視窗