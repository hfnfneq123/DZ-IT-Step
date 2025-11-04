import cv2
from PIL import Image

image_path = 'img_1.png'

man_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread(image_path)
man_face_face = man_face.detectMultiScale(image)

man = Image.open(image_path)
mask = Image.open('mask.png')
man = man.convert("RGBA")
mask = mask.convert("RGBA")

for (x, y, w, h) in man_face_face:
    mask = mask.resize((w, int(h/1.5)))
    man.paste(mask, (x, int(y + h / 20)), mask)
man.save("man_new.png")
man_new = cv2.imread("man_new.png")
cv2.imshow("Man with Mask", man_new)
cv2.waitKey(0)
