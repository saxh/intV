import os
import cv2

if __name__ == '__main__':
    for root, file, filenames in os.walk("./play/"):
        for filename in filenames:
            filename1 = os.path.join("play/", filename)
            img = cv2.imread(filename1)

            img = cv2.resize(img, (351, 400))
            cv2.imwrite(os.path.join("play/", 'new' + filename), img)
