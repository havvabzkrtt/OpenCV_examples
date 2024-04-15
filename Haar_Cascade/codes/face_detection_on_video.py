import cv2   

# kullanılacak video
vid = cv2.VideoCapture("test_videos/faces.mp4")

# haar cascade dosyası
face_cascade = cv2.CascadeClassifier("haarCascade/frontalface.xml")

# sonsuz bir döngü ile her karey(frame) tek tek incelenir
while 1:
    
    # her karey tek tek okunur
    _, frame = vid.read()
    
    # haar-like özellikleri kolay algılanması için her bir karey boz(gri) tonlara çevirilir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # cascade dosyası kullanılarak her bir kare üzerindeki yüzlerin koordinarlarını bulunur
    faces = face_cascade.detectMultiScale(gray, 1.2, 1)

    # "faces" tuple'ında tutulan koordinatlar kullanılarak yüzler dikdörtgen içerisine alınır
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
    # işlediğimiz kareler
    cv2.imshow('video',frame)

    # programı kapatacak kodu
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# videoyu serbest bırakılır
vid.release()
cv2.destroyAllWindows()
