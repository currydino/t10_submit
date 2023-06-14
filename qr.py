
import pip
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
install('qrcode pillow') #qr코드 제작을 위한 pip

import qrcode
website_link ='https://currydino-team10-info-0i61s0.streamlit.app/'
qr = qrcode.QRCode(version = 1, box_size = 5, border = 5) #qr코드의 박스사이즈
qr.add_data(website_link)
qr.make()#큐알 제작
img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('swu.png')
