import cv2
from gesture_detection import detect_gesture
from key_controller import press_space
from utils import FPSCounter

def main():
    cap = cv2.VideoCapture(0)
    fps_counter = FPSCounter()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gesture, frame = detect_gesture(frame)

        if gesture == "flap":
            press_space()

        fps = fps_counter.update()
        cv2.putText(frame, f'FPS: {fps}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Hand Gesture Control', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
