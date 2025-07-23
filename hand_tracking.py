import cv2
import mediapipe as mp
import pygame



# Initialize pygame sound.
pygame.mixer.init()
sound = pygame.mixer.Sound("beep.wav")

# Setup MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Drawing constants
CIRCLE_COLOR = (255, 0, 255)
CIRCLE_RADIUS = 80
CIRCLE_THICKNESS = 2
FINGER_TIP_ID = 8  # Index finger tip


# Run the webcam.
cap = cv2.VideoCapture(0)

# Main event loop.
while True:

    # Get a frame from the webcam.
    ret, frame = cap.read()
    if not ret:
        break

    # Flip it for selfie view.
    frame = cv2.flip(frame, 1)

    # Get the center of the image for drawing the circle.
    h, w, _ = frame.shape
    cx, cy = w // 2, h // 2

    # Draw the circle.
    cv2.circle(frame, (cx, cy), CIRCLE_RADIUS, CIRCLE_COLOR, CIRCLE_THICKNESS)

    # Hand tracking.
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    # If a hand is detected, proceed!
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:

            # Draw landmarks (circles).
            for id, lm in enumerate(hand_landmarks.landmark):
                x, y = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

            # Draw connections (lines between circles).
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(0,0,255), thickness=2)
            )

            # Get the index fingertip position.
            tip = hand_landmarks.landmark[FINGER_TIP_ID]
            tip_x, tip_y = int(tip.x * w), int(tip.y * h)

            # Check if it's inside center circle.
            dist = ((tip_x - cx)**2 + (tip_y - cy)**2)**0.5
            if dist < CIRCLE_RADIUS:
                sound.play()

    # Show image (ESC to quit)
    cv2.imshow("Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Clean-up when quit.
cap.release()
cv2.destroyAllWindows()
