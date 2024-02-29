import cv2
import streamlit as st
import mediapipe as mp

st.title("Webcam Live Feed")

cap = cv2.VideoCapture(0)

frame_placeholder = st.empty()
stop_button_pressed = st.button("stop")
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

with mp.solutions.hands.Hands(
    # Parametro para especificar la complejidad del modelo usado en la detección de las manos
    model_complexity=1,
    min_detection_confidence=0.3,
    min_tracking_confidence=0.6
) as mp_hands:
    while True:
        # Read Camera
        _, frame = cap.read()

        # Predict hand landmarks
        frame.flags.writeable = False
        # Conversion the Frame from BGR to RGB
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = mp_hands.process(frame)

        # Draw the annotations on the image
        image = frame.flags.writeable = True
        image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp.solutions.hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

        frame_placeholder.image(cv2.cvtColor(image,cv2.COLOR_BGR2RGB), channels="RGB")
        if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
            break
cap.release()
cv2.destroyAllWindows()