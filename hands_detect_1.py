# pip install mediapipe
import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

# mediapipe 手掌偵測
mp_hand = mp.solutions.hands
hands = mp_hand.Hands()

while True:
    success, img = cap.read()

    if not success:
        break

    # 按下 q 鍵停止
    if cv2.waitKey(1) == ord('q'):
        break

    result = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    hand_landmarks = result.multi_hand_landmarks
    print(hand_landmarks)

    cv2.imshow("hands detection", img)

cap.release()
cv2.destroyAllWindows()