from PIL import Image #Download Pillow
import ImageTools #Download ImageToolsMadeEasy

#Take photo of user
camera = ImageTools.Camera()
img = camera.take_photo()

#ID face of user photo
faces = ImageTools.get_faces(img, "haarcascade_frontalface_default.xml")

#Paste cropped eyes around all faces in original image
for face in faces:
    x, y, w, h = face
    face_only = img.crop((x+0.1*w, y+0.2*h, x+0.9*w, y+0.5*h))

    xMidRight = (x+ 0.5*w) + 0.35*w
    xMidLeft = (x+ 0.5*w) - 1.15*w
    xOutRight = (x+ 0.5*w) + 0.15*w
    xOutLeft = (x+ 0.5*w) - 0.95*w
    yMiddle = y + h* 0.2
    yTop = y
    yBottom = y + h*0.4


    img.paste(face_only, (xOutRight.astype(int), yBottom.astype(int)))
    img.paste(face_only, (xOutLeft.astype(int), yBottom.astype(int)))

    img.paste(face_only, (xMidRight.astype(int), yMiddle.astype(int)))
    img.paste(face_only, (xMidLeft.astype(int), yMiddle.astype(int)))


    img.paste(face_only, (xOutRight.astype(int), yTop.astype(int)))
    img.paste(face_only, (xOutLeft.astype(int), yTop.astype(int)))

#show final image with filter
img.show()
