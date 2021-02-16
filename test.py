
import cat_predict as cat
import color_re as ct
# import ulf_predict as ulf
import att_predict as att
import cloth_matching_weather as cmw

import weather_matching_cloth_table as wmc_table  # 날씨별 옷 추천(테이블)
import weather_matching_cloth_txt as wmc_txt  # 날씨별 옷 추천(텍스트)

import news_ai as news
import live_rank_ai as rank

def parsing(text):
    if '종류' in text:
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
    elif '뉴스' in text:
        return 7
    elif '검색' in text:
        return 8

    elif text == "":
        return -1
    else:
        return -1
    
def select_func(num):

    weather_txt = cmw.matching_weather()
    recommand_table = list()
    recommand_table = wmc_table.weather_matching()
    weather_ment, recommand_txt = wmc_txt.weather_matching()

    # ui.print_ui(cat_txt, att_txt, cat_score, att_score, color_txt)
    # # ui.print_ui(cat_txt, att_txt, color_txt)

    if num == 1:  # 종류
        speech_txt = '당신이 고른 의상의 속성은 노랑입니다.\n'
    elif num == 2:  # 속성
        speech_txt = '당신이 고른 의상의 속성은 노랑입니다.\n'
    elif num == 3:  # 색상
        speech_txt = '당신이 고른 의상의 속성은 노랑입니다.\n'
    elif num == 4:  # 인식한 옷의 날씨 적합성
        speech_txt = '당신이 고른 의상의 속성은 노랑입니다.\n'
    elif num == 5:  # 정보(1~4 합친것)
        speech_txt = '당신이 고른 의상의 속성은 노랑입니다.\n'
    elif num == 6:  # 추천
        speech_txt = '당신이 고른 의상의 속성은 노랑입니다.\n'
        print(recommand_table)
    elif num==7:    #뉴스 토픽
        speech_txt = str(news.news_topik())
    elif num==8:
        speech_txt = str(rank.live_rank())

    print(speech_txt)
    print('finish')
    
select_func(parsing('순위를 알려줘'))
