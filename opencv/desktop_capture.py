# -*- coding: utf-8 -*-
import cv2
import numpy as np
import ImageGrab

def main():

    while(1):
        im = ImageGrab.grab((0, 0, 400, 300))   # デスクトップの始点(0,0),横400, 縦300の矩形部分をキャプチャ
        im = np.asarray(im)                     # OpenCVで扱うためにNumpy配列に変換
        cv2.imshow("desktop", im)               # 画面表示
        if cv2.waitKey(1) > 0:                  # キー入力があれば終了
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    main()
