
import cv2
import glob
path = "D:\python\images\wallpapers\*.*"
for file in glob.glob(path):
   print(file)
   a= cv2.imread(file)
   print(a)
   cv2.imshow('Color image', a)
   k = cv2.waitKey(0)
   cv2.destroyAllWindows()