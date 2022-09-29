import cv2


image = str(input("Унесите име генерисане слике са QR кодом: "))

img = cv2.imread(image) # учитавање слике са QR кодом

detector = cv2.QRCodeDetector()

data, bbox, straight_qrcode = detector.detectAndDecode(img)

if bbox is not None:
    
    print(f"[+] QR dekodiran: {data}") # штампање декориданих података

    n_lines = len(bbox)
    
    for i in range(n_lines):

        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
        cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)

cv2.imshow("QR", img) # приказ учитане слике
cv2.waitKey(0)
cv2.destroyAllWindows()        
