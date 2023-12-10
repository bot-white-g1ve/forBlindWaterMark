from blind_watermark import WaterMark
import time
from PIL import Image
import sys

def encodestr(img,str):#嵌入文字信息
    startime = time.time()
    bwm1 = WaterMark(password_img=1, password_wm=1)
    bwm1.read_img('input/'+img)
    bwm1.read_wm(str, mode='str')
    bwm1.embed('output/embedded.png')
    len_wm = len(bwm1.wm_bit)
    print('Put down the length of wm_bit {len_wm}'.format(len_wm=len_wm))
    encodetime = time.time()
    print("encode time ", encodetime - startime)
    return len_wm
def decodestr(img,len):#解密文字信息
    startime=time.time()
    bwm1 = WaterMark(password_img=1, password_wm=1)
    wm_extract = bwm1.extract('output/'+img, wm_shape=int(len), mode='str')
    endtime = time.time()
    costtime = endtime - startime
    print("time cost:", costtime)
    print("the string extracted: ", wm_extract)
def encodeimg(carrier,watermark):#嵌入图像水印
    startime = time.time()
    bwm1 = WaterMark(password_wm=1, password_img=1)
    # 读取原图
    bwm1.read_img('input/'+carrier)
    # 读取水印
    bwm1.read_wm('img_wm/input/'+watermark)
    # 打上盲水印
    bwm1.embed('output/embedded.png')
    endtime = time.time()
    costtime = endtime - starttime
    print("time cost: ", costtime)
    with Image.open(watermark) as img:
        print("watermark's size: ", img.size)
def decodeimg(img, size):#提取图像水印
    bwm1 = WaterMark(password_wm=1, password_img=1)
    # 注意需要设定水印的长宽wm_shape
    bwm1.extract(filename=img, wm_shape=size,out_wm_name='img_wm/output/extracted.png')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("no arguments")
        sys.exit(0)
    if sys.argv[1] == 'encodestr':
        encodestr(sys.argv[2], sys.argv[3])
    if sys.argv[1] == 'decodestr':
        decodestr(sys.argv[2], sys.argv[3])
    else:
        print("wrong arguments")