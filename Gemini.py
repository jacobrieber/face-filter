from PIL import Image #Download Pillow
import ImageTools #Download ImageToolsMadeEasy

#Take photo
camera = ImageTools.Camera()
img = camera.take_photo()

#ID face of user photo
faces = ImageTools.get_faces(img, "haarcascade_frontalface_default.xml")

#Paste cropped images of face around all faces in the photo
for face in faces:
    x, y, w, h = face
    justFace = img.crop((x, y, x+w, y+h))


    xRight1 = (x+ 0.5*w) + 0.3*w
    xLeft1 = (x+ 0.5*w) - 1.3*w

    xRight2 = (x+ 0.5*w) + 0.5*w
    xLeft2 = (x+ 0.5*w) - 1.5*w

    img.paste(justFace, (xLeft1.astype(int), y))
    img.paste(justFace, (xRight1.astype(int), y))

    img.paste(justFace, (xLeft2.astype(int), y))
    img.paste(justFace, (xRight2.astype(int), y))

#show final image with filter
img.show()
