from blind_watermark import WaterMark

bwm1 = WaterMark(password_img=1, password_wm=1)
bwm1.read_img('input/ori_img.jpeg')
wm = '@guofei9987 开源万岁！'
bwm1.read_wm(wm, mode='str')
bwm1.embed('output/embedded.png')
len_wm = len(bwm1.wm_bit)
print('Put down the length of wm_bit {len_wm}'.format(len_wm=len_wm))

bwm2 = WaterMark(password_img=1, password_wm=1)
wm_extract = bwm2.extract('output/embedded.png', wm_shape=len_wm, mode='str')
print(wm_extract)
