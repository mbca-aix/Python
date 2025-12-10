# pyinstaller 모듈을 이용하여 실행파일을 만들면. 기존에 사용하단 상대경로가 맞지 않게됨
# 파이썬 만의 특정 폴더 영역으로 리소스(이미지,동영상,음성,폰트 파일들)를 위치한 후 실행함
# 그래서 코드에서.. 이 경로를 기반으로 리소스의 경로를 지정해야 함.

import sys
import os

# 상대경로를 파라미터로 받아서 리소스용 경로를 만들어주는 기능함수를 미리 정의
def resource_path( path ):
    try:
        base_path= sys._MEIPASS
    except:
        base_path= os.path.abspath('.')
    
    #2개의 경로를 합성해주는 기능
    return os.path.join(base_path, path)

from tkinter import *

window= Tk()

img= PhotoImage(file=resource_path('resources/image/ms19.png'))
label= Label(window, image=img)
label.pack()

img2= PhotoImage(file=resource_path('resources/image/dao.png'))
label2= Label(window, image=img2)
label2.pack()

window.mainloop()
