import cv2

image = cv2.imread("input.png")
detector = cv2.QRCodeDetector()

data, bbox, _ = detector.detectAndDecode(image)

if bbox is not None:
    bbox = bbox.astype(int)
    for i in range(len(bbox[0])):
        cv2.line(image, tuple(bbox[0][i]),
                 tuple(bbox[0][(i + 1) % 4]),
                 (0, 0, 255), 5)
    if data:
        cv2.putText(image, data, (bbox[0][0][0], bbox[0][0][1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        print(f"QR Kod Verisi: {data}")
else:
    print("QR kod bulunamadı.")

cv2.imshow("QR Scanner", image)
cv2.imwrite("output.png", image)
cv2.waitKey(0)
cv2.destroyAllWindows()