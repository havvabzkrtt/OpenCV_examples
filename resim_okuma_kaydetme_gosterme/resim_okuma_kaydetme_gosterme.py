import cv2

#img = cv2.imread("klon.jpg")  # resim okuma  # resimadi, gri ton
img = cv2.imread("klon.jpg", cv2.IMREAD_GRAYSCALE) # siyah beyaz
#img = cv2.imread("klon.jpg", cv2.0) # siyah beyaz
# print(img) # resmin piksel değerlerini verir
#img = cv2.imread("C:/Users/HP/Desktop/klon.jpg") # resmin adresinden okuma

cv2.namedWindow("Image",cv2.WINDOW_NORMAL) # olusturulacak pencerenin adi, pencerenin yeniden boyutlandılabilecegini gösteren flag degeri

cv2.imshow("Image",img) # resmi gösterme # resmin gösterileceği ekran adi, resim degiskeni

#cv2.imwrite("klon1.jpg",img) # resmi kaydetme # resim kaydeilecek ad, resim degiskeni
cv2.imwrite("C:/Users/HP/Desktop/klon1.jpg",img) # resmi bir adrese kaydetme

cv2.waitKey(0) # 0 değeri ile ekranı kaptana kadar ekranda durur, ya da içinde yazılan milisaniye kadar ekranda açık durur

cv2.destroyWindow()   # örnegin q tusuna basinca tüm pencereler kapansin kodu yazdık bunu çalıstırır, her kodun sonuna yazılmalı aslında hatalardan kaçmak için

