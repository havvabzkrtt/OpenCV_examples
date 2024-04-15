import cv2


# test image
img = cv2.imread("test_images/face.png")

# haar cascade dosyası 
face_cascade = cv2.CascadeClassifier("haarCascade/frontalface.xml")


# convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# yüz koordinatlarını bulunur ve bir tuple a aktarılır
faces = face_cascade.detectMultiScale(gray, 1.3, 7)  # Bellirli bir bölgede en az 7 pencere yüz bulur, daha iyi sonuçlar elde etmek için bu değer arttırılabilir. (4 iken, 2 yüz buluyordu.)

# "faces" tuple'ında tutulan koordinatlar kullanılarak yüzler dikdörtgen içerisine alınır
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2) # (image, genişlik ve yükseklik için koordinatlar, renk, kalınlık)

# show image
cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()