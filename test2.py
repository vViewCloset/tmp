import socket
import os
import time
import numpy as np
import cv2
#import ulf_predict as ulf
import cloth_matching_weather as cmw
#import weather_matching_cloth_table as wmc_table # 날씨별 옷 추천(테이블)
import weather_matching_cloth_txt as wmc_txt # 날씨별 옷 추천(텍스트)
#import weather_matching_cloth_test as wmc_test
#import make_ui_JD as ui
from threading import Thread

def select_func(num):
    weather_txt = cmw.matching_weather()
    #recommand_table = list()
    #recommand_table = wmc_table.weather_matching()
    kkk = wmc_txt.weather_matching()

    #ui.print_ui(cat_txt, att_txt, cat_score, att_score, color_txt)

    if num == 1:  # 종류
        speech_txt = '당신이 고른 의상의 종류는 ' + cat_txt + ' 입니다.\n'
    elif num == 4:  # 인식한 옷의 날씨 적합성
        speech_txt = weather_txt
    elif num == 6:  # 추천
        speech_txt = kkk
        #print(recommand_table)

    audio_s.send_text(speech_txt)
    print(speech_txt)
    print('finish')

if __name__ == "__main__":
    select_func(6)
