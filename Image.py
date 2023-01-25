import cv2
import glob
import numpy

img=cv2.imread("image1.JPG", 1)

print(type(img))
print(img)
print(img.shape)
a = img.ndim
print(a)

resize_img=cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Ground", resize_img)
cv2.imwrite("resized.jpg", resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


images= glob.glob("sample/*.jpg")

for image in images:
    img2=cv2.imread(image, 0)
    re = cv2.resize(img2,(500,500))
    cv2.imshow("oktested", re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwritemulti("re_"+image, re)

img3=numpy.random.randint(255, size=(500, 500, 3))
cv2.imwrite("sample/image1.jpg", img3)