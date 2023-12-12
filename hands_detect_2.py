import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_hand = mp.solutions.hands                     # mediapipe 手掌偵測
mp_drawing_utils = mp.solutions.drawing_utils    # mediapipe 繪圖工具
mp_drawing_styles = mp.solutions.drawing_styles  # mediapipe 繪圖樣式

# 這邊有一些參數可以自行調整
hands = mp_hand.Hands(
    static_image_mode = False,       # False = 動態(影片)，True = 靜態(圖片)
    model_complexity = 0,            # 精準度 0 or 1，越大越精準
    max_num_hands = 2,               # 偵測幾隻手
    min_detection_confidence = 0.5,  # 偵測手掌的最低自信度，0~1，越大判定越嚴格
    min_tracking_confidence = 0.5    # 追蹤座標的最低自信度，0~1，越大判定越嚴格
)

while True:
    success, img = cap.read()

    if not success:
        break

    # 按下 q 鍵停止
    if cv2.waitKey(1) == ord('q'):
        break             

    result = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    hand_landmarks = result.multi_hand_landmarks
    
    if (hand_landmarks):
        for hand_landmark in hand_landmarks:
            # # 將節點和骨架繪製到影像中
            mp_drawing_utils.draw_landmarks(
                img,
                hand_landmark,
                mp_hand.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

    cv2.imshow("hands detection", img)
    
cap.release()
cv2.destroyAllWindows()