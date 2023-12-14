import cv2

cap = cv2.VideoCapture(0)  # 鏡頭的編號，通常都從 0 開始

while True:
    success, img = cap.read()  # 讀取影片的每一幀

    if not success:
        break

    # 按下 q 鍵停止
    if cv2.waitKey(1) == ord('q'):
        break

    # 轉換成灰階
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Video", img)
    
cap.release()
cv2.destroyAllWindows()