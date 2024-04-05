import cv2
import matplotlib.pyplot as plt

gray_img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)


# GAUSS 
filtered_gauss3 = cv2.GaussianBlur(gray_img, (3,3),0)
edge_gauss3 = cv2.Canny(filtered_gauss3, 20, 30)
cv2.imwrite('canny_gauss_3.png',edge_gauss3)

edge_gauss3x = cv2.Canny(filtered_gauss3, 50, 60)
cv2.imwrite('canny_gauss_3x.png',edge_gauss3x)


filtered_gauss5 = cv2.GaussianBlur(gray_img, (5,5),0)
edge_gauss5 = cv2.Canny(filtered_gauss5, 20, 30)
cv2.imwrite('canny_gauss_5.png',edge_gauss5)

edge_gauss5x = cv2.Canny(filtered_gauss5, 50, 60)
cv2.imwrite('canny_gauss_5x.png',edge_gauss5x)


# MEAN
filtered_mean3 = cv2.blur(gray_img,(3,3))
edge_mean3 = cv2.Canny(filtered_mean3, 20, 30)
cv2.imwrite('canny_mean_3.png',edge_mean3)

edge_mean3x = cv2.Canny(filtered_mean3, 50, 60)
cv2.imwrite('canny_mean_3x.png',edge_mean3x)

filtered_mean5 = cv2.blur(gray_img,(5,5))
edge_mean5 = cv2.Canny(filtered_mean5, 20, 30)
cv2.imwrite('canny_mean_5.png',edge_mean5)

edge_mean5x = cv2.Canny(filtered_mean5, 50, 60)
cv2.imwrite('canny_mean_5x.png',edge_mean5x)


#MEDIAN
filtered_median3 = cv2.medianBlur(gray_img, 3)
edge_median3 = cv2.Canny(filtered_median3, 20, 30)
cv2.imwrite('canny_median_3.png',edge_median3)

edge_median3x = cv2.Canny(filtered_median3, 50, 60)
cv2.imwrite('canny_median_3x.png',edge_median3x)

filtered_median5 = cv2.medianBlur(gray_img, 3)
edge_median5 = cv2.Canny(filtered_median5, 20, 30)
cv2.imwrite('canny_median_5.png',edge_median5)

edge_median5x = cv2.Canny(filtered_median5, 50, 60)
cv2.imwrite('canny_median_5x.png',edge_median5x)



