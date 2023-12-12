import cv2
import numpy as np

# 開啟圖片
img = cv2.imread("./images/kekw.jpg")  # cv2.IMREAD_COLOR (BGR)

# 對比 & 亮度 (要搭配 numpy)
# pip install numpy
contrast = 200
brightness = 100
enhance = img * (contrast/127 + 1) - contrast + brightness # 轉換公式

# 調整後的數值大多為浮點數，且可能會小於 0 或大於 255
# 為了保持像素色彩區間為 0～255 的整數，所以再使用 np.clip() 和 np.uint8() 進行轉換
enhance = np.clip(enhance, 0, 255)
enhance = np.uint8(enhance)

cv2.imshow("The Image", enhance)  # 使用視窗開啟圖片
cv2.waitKey(0)                # 按下任意鍵停止
cv2.destroyAllWindows()       # 結束所有圖片視窗