# -*- coding: utf-8 -*-
import cv2

def main():
    im = cv2.imread("test.jpg")                     # 画像の読み込み
    cv2.pyrMeanShiftFiltering(im, 20, 200, im, 2)   # MeanShiftで領域分割
    cv2.imshow("Keypoint",im)                       # ウィンドウの表示
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
