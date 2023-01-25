import cv2

face_cascade= cv2.CascadeClassifier("sample/haarcascade_frontalface_default.xml")

img = cv2.imread("sample/Stuff/photo.jpg")
gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_image, scaleFactor=1.05, minNeighbors=5)

for x,y,w,h in faces:
    img=cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)


print(type(faces))
print(faces)

resized_img=cv2.resize(img, (250,250))

cv2.imshow("pixel", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("pixel2", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


img2=cv2.imread("sample/Stuff/news.jpg")

faces2=face_cascade.detectMultiScale(img2, scaleFactor=1.15, minNeighbors=5)
print(type(faces2))
print(faces2)

for x,y,w,h in faces2:
    img2=cv2.rectangle(img2, (x,y), (x+w, y+h), (0,255,0), 2)

resize_img2=cv2.resize(img2, (500,500))

cv2.imshow("pixel3", resize_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
