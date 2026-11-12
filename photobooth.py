import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("kamera tidak terdeteksi!")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("tekan 'c' untuk CAPTURE")
print("tekan 'q' untuk CAPTURE\n")

while True:
    ret, frame = cap.read()

    cv2.imshow("photobooth", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
          nama_file = f"foto_{datetime.now().strftime('%H%M%S')}.jpg"
          cv2.imwrite(nama_file, frame)
          print(f"tersimpan: {nama_file}")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("program selesai!")