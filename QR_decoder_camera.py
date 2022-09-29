import cv2


kamera = cv2.VideoCapture(0) # иницијализација USB камере
detector = cv2.QRCodeDetector()

while True:
    
    success , img = kamera.read()
    data, bbox, _ = detector.detectAndDecode(img)
    
    if bbox:

        for i in range(len(bbox)):
            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
            
        if data:
            print(f"[+] QR dekodiran: {data}") # штампање декориданих података

    cv2.imshow("QR", img) # приказ stream-а са камере
    
    if cv2.waitKey(1) == ord("q"): # тастер 'q' са тастатуре прекида скенирање
        break
    
cap.release()
cv2.destroyAllWindows()
