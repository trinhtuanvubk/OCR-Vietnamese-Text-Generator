import cv2

path = "./out/dataset/17.jpg"
im = cv2.imread(path)
print(im.shape)