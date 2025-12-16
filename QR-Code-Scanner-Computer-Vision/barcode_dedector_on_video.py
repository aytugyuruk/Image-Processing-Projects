import cv2

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # QR kodu tespit et
    data, bbox, _ = detector.detectAndDecode(frame)

    # Eğer QR kod bulunduysa kare çiz
    if bbox is not None:
        bbox = bbox.astype(int)
        for i in range(len(bbox[0])):
            cv2.line(frame, tuple(bbox[0][i]),
                     tuple(bbox[0][(i+1) % 4]),
                     (0, 0, 255), 5)
        if data:
            cv2.putText(frame, data, (bbox[0][0][0], bbox[0][0][1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,255),3)

    cv2.imshow("QR Scanner", frame)

    # 'q' tuşuna basınca çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()