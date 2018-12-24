import cv2
import numpy as np

def barline(height: object = 40, width: object = 500):

    # widthサイズの0~180の数列を作成
    h = np.linspace(0, 180, width)
    # widthサイズの255埋め配列を作成
    s = np.full(width, 255)
    # widthサイズの255埋め配列を作成
    v = np.full(width, 255)
    # h,s,vを結合して転置する(高さ1分のデータを作成)
    bar1 = np.vstack((h, s, v)).transpose()
    # heigth分に拡張しuint8に変換
    bar = np.tile(bar1, (height, 1, 1)).astype(np.uint8)

    # start_list = (0, 255, 255)
    # stop_list = (180, 255, 255)

    # height,width分のデータを作っておく
    # bar =np.zeros((height, width, len(start_list)), dtype=np.uint8)
    # h,s,vの三回繰り返す
    # for i, (start, stop) in enumerate(zip(start_list, stop_list)):
    # startからstopまでの等差数列を作成して入れる(i=0はh,i=1はs,i=2はv)
    #     bar[:, :, i] = np.tile(np.linspace(start, stop, width), (height, 1))

    # HSVからRGBに色空間を変更する
    hsv = cv2.cvtColor(bar, cv2.COLOR_HSV2BGR)
    return hsv

def main():
    cv2.imshow('tmp', barline())
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()