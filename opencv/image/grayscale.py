# -*- coding: utf-8 -*-
import cv2

def main():
    im = cv2.imread("test.jpg")                 # 画像を読み込み
    gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)   # RGB画像をグレースケールに変換
    cv2.imshow("Show",gray)                       # ウィンドウの表示
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
