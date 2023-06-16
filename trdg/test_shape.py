import cv2

path = "./out/dataset/182.jpg"
im = cv2.imread(path)
print(im.shape)