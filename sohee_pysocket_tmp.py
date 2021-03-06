import socket
import os
import time
import numpy as np
import cv2
import cat_predict as cat
import color_re as ct
#import ulf_predict as ulf 
import att_predict as att
import cloth_matching_weather as cmw

import weather_matching_cloth_table as wmc_table # 날씨별 옷 추천(테이블)
import weather_matching_cloth_txt as wmc_txt # 날씨별 옷 추천(텍스트)

import make_ui_JD as ui
from threading import Thread


class Server:
    def __init__(self, port):
        self.ip = ''
        self.port = port
        self.serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        self.serv_sock.bind((self.ip, self.port))
        self.serv_sock.listen(5)
        self.client_sock = None

    def sock_listen(self):
        self.client_sock,addr = self.serv_sock.accept()

        if self.port == 5241:
            print('[ ROSE ] : Image Client Connected! ')
        else:
            print('[ ROSE ] : Text Client Connected! ')
        
        return True

    def recvall(self, count):
        buf = b''
        while count:
            newbuf = self.client_sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf
    
    def recv_image(self):
        length = self.recvall(16)
        stringData = self.recvall(int(length))
        data = np.frombuffer(stringData, dtype='uint8')

        decimg=cv2.imdecode(data, 1)
        #cv2.imshow('Image', decimg)
        cv2.imwrite('camera.png', decimg)

        
        '''sz = ""
        f = open('camera.png', 'wb')
        #data = self.client_sock.recv(15)

        #sz = data.decode()
        #print(sz)
        
        #with open('camera.png', 'wb') as f:
            #data = self.client_sock.recv(330397)
            #f.write(data)
            #print('[ ROSE ] : picture recvied correctly!!')
            #f.close()

        while True:
            temp = self.client_sock.recv(1024)
            #print('[ ROSE ] : picture recvied correctly!!')
            #file_sz += temp.decode()
            #break
            #print(str(temp.decode()))
            
            if not temp:
                print('[ ROSE ] : picture recvied correctly!!')
                break
            else:                   
                f.write(temp)
                
        
        f.close()'''
        
  
    def recv_text(self):
        str = ""

        while True:
            data = self.client_sock.recv(1024)
            str += data.decode()
            print('[ ROSE ] : text: ', str)

            break

            if not data:             
                break
            str = ""

        if str != "" :   
            print('[ ROSE ] : text: ', str)
        
        return str
    
    def send_text(self, str):
        #str = "hi hello nice to meet you"
        self.client_sock.send(str.encode())
        
    def __del__(self):
        self.serv_sock.close()

        
def image_thread():
    camera_s = Server(5241)
    camera_s.sock_listen()

    while True:
        camera_s.recv_image()

    
def text_thread():
    audio_s = Server(5242)
    audio_s.sock_listen()

    while True:
        str = audio_s.recv_text()
        #
        #
        audio_s.send_text(str)
        print('finish')

def parsing(text):
    if '종류'in text:
        return 1 
    elif '속성' in text:
        return 2
    elif '색상' in text:
        return 3
    elif '날씨' in text:
        return 4
    elif '정보' in text:
        return 5
    elif '추천' in text:
        return 6
    elif text == "":
        return -1
    else: 
        return -1

def select_func(num):
    cat_txt,cat_score = cat.category_total()
    att_txt,att_score = att.attribute_total()
    color_txt = ct.color_total()
    weather_txt = cmw.matching_weather()
    recommand_table = list()
    recommand_table = wmc_table.weather_matching()
    weather_ment, recommand_txt = wmc_txt.weather_matching()

    ui.print_ui(cat_txt, att_txt,cat_score,att_score,color_txt)
    #ui.print_ui(cat_txt, att_txt, color_txt)
 

    if num == 1: # 종류
        speech_txt = '당신이 고른 의상의 종류는 ' + cat_txt + ' 입니다.\n'
    elif num == 2: # 속성
        speech_txt = '당신이 고른 의상의 속성은 ' + att_txt + ' 입니다.\n'
    elif num == 3: # 색상
        speech_txt = '당신이 고른 의상은 ' + color_txt + ' 색상 입니다.\n'
    elif num == 4: # 인식한 옷의 날씨 적합성
        speech_txt = weather_txt 
    elif num == 5: # 정보(1~4 합친것)
        speech_txt = '\n당신이 고른 의상은' + color_txt + ' 색상의 ' + cat_txt + ' 이고,\n\n' + att_txt + ' 속성에 해당합니다.\n\n날씨별 적합성을 알려드리겠습니다.\n' + weather_txt 
    elif num == 6: # 추천
        speech_txt = weather_ment + recommand_txt
        print(recommand_table)

    audio_s.send_text(speech_txt)
    print(speech_txt)
    print('finish')

if __name__ == "__main__":
    #th1 = Thread(target=image_thread, args=())
    #th2 = Thread(target=text_thread, args=())

    #th1.start()

    camera_s = Server(5241)
    audio_s = Server(5242)
    camera_s.sock_listen()   
    audio_s.sock_listen()

    while True:
	# receive txt
        voice_txt=audio_s.recv_text()
        num = parsing(voice_txt) 
        if(num>0):
            audio_s.send_text('YES')
            camera_s.recv_image()
	#camera_s.recv_image()
        else:
            audio_s.send_text('NO')
            continue;
		
    # here
      #  voice_txt
        select_func(num)  
    #th2.start()
        
    #th1.join()
    #th2.join()

'''
ip = ''
port = 5241
serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
serv_sock.bind((ip, port))
serv_sock.listen(5)
data = ""

i = 0

while i < 5:
    client_sock,addr = serv_sock.accept()
   
    f = open('camera.png', 'wb')
    
    while True:
        temp = client_sock.recv(1024)
        if temp:
            f.write(temp)
        else:
            break

    f.close
    i = i+1
'''


