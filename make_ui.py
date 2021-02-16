import att_predict as ap
import cat_predict as cp
import color_re as cr

def ui_short(cat,att,color):
    att_len = 13; cat_len = 13; color_len = 19
    #att = 'leopard'; cat = 'dress'; color = 'darkseagreen'

    #print('berfore', len(att), len(cat), len(color))
    if len(att) % 2 == 0:
        att = att + ' '

    if len(cat) % 2 == 0:
        cat = cat + ' '

    if len(color) % 2 == 0:
        color = color + ' '

    #print('after', len(att), len(cat), len(color))

    att_blank = int((att_len - len(att))/2)
    cat_blank = int((cat_len - len(cat))/2)
    color_blank = int((color_len - len(color))/2)

    #print('att_blank:',att_blank, 'cat_blank: ',cat_blank, 'color_blank: ',color_blank)
    att_list = []; cat_list = []; color_list = []

    for i in range(att_blank):
        att_list.append(' ')

    att_list.append(att)

    for i in range(att_blank):
        att_list.append(' ')

    att_txt = ''.join(att_list)

    for i in range(cat_blank):
        cat_list.append(' ')

    cat_list.append(cat)

    for i in range(cat_blank):
        cat_list.append(' ')

    cat_txt = ''.join(cat_list)

    for i in range(color_blank):
        color_list.append(' ')

    color_list.append(color)

    for i in range(color_blank):
        color_list.append(' ')

    color_txt = ''.join(color_list)

    print(' -----------------------------------------------')
    print('|     속성    |     종류    |        색상       |')
    print(' -----------------------------------------------')
    print('|' + att_txt + '|' + cat_txt + '|' + color_txt + '|')
    print(' -----------------------------------------------')

def ui_long(cat, att, color):
    att_len = 17; cat_len = 17; color_len = 23

    if len(att) % 2 == 0:
        att = att + ' '

    if len(cat) % 2 == 0:
        cat = cat + ' '

    if len(color) % 2 == 0:
        color = color + ' '
    
    att_blank = int((att_len - len(att))/2)
    cat_blank = int((cat_len - len(cat))/2)
    color_blank = int((color_len - len(color))/2)

    #print('att_blank:',att_blank, 'cat_blank: ',cat_blank, 'color_blank: ',color_blank)
    att_list = []; cat_list = []; color_list = []

    for i in range(att_blank):
        att_list.append(' ')

    att_list.append(att)

    for i in range(att_blank):
        att_list.append(' ')

    att_txt = ''.join(att_list)

    for i in range(cat_blank):
        cat_list.append(' ')

    cat_list.append(cat)

    for i in range(cat_blank):
        cat_list.append(' ')

    cat_txt = ''.join(cat_list)

    for i in range(color_blank):
        color_list.append(' ')

    color_list.append(color)

    for i in range(color_blank):
        color_list.append(' ')

    color_txt = ''.join(color_list)

    print(' -----------------------------------------------------------')
    print('|       속성      |       종류      |          색상         |')
    print(' -----------------------------------------------------------')
    print('|' + att_txt + '|' + cat_txt + '|' + color_txt + '|')
    print(' -----------------------------------------------------------')


''' test '''
#color = 'violetddddddddddddddd'
color = cr.color_total()
att = ap.attribute_total()
cat = cp.category_total()

def print_ui(cat,att,color):
    if len(att) >= 13 or len(cat) >= 13 or len(color) >=19:
        ui_long(cat,att,color)
    else:
        ui_short(cat,att,color)
