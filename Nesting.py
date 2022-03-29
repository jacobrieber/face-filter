from PIL import Image #Download Pillow
import ImageTools #Download ImageToolsMadeEasy

#Take photo
camera = ImageTools.Camera()
img = camera.take_photo()

#ID face of user photo
faces = ImageTools.get_faces(img, "haarcascade_frontalface_default.xml")

#Paste cropped halves of each face around all faces in the image
for face in faces:
    x, y, w, h = face
    leftHalf = img.crop((x, y, x+0.5*w, y+h))
    rightHalf = img.crop((x+0.5*w, y, x+w, y+h))

    xRight1 = (x+ 0.5*w) + 0.3*w
    xLeft1 = (x+ 0.5*w) - 0.8*w

    xRight2 = (x+ 0.5*w) + 0.45*w
    xLeft2 = (x+ 0.5*w) - 0.95*w

    xRight3 = (x+ 0.5*w) + 0.6*w
    xLeft3 = (x+ 0.5*w) - 1.1*w

    img.paste(leftHalf, (xLeft1.astype(int), y))
    img.paste(rightHalf, (xRight1.astype(int), y))

    img.paste(leftHalf, (xLeft2.astype(int), y))
    img.paste(rightHalf, (xRight2.astype(int), y))

    img.paste(leftHalf, (xLeft3.astype(int), y))
    img.paste(rightHalf, (xRight3.astype(int), y))

#show final image with filter
img.show()
