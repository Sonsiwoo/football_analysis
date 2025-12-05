import json 
from urllib.request import urlopen


import matplotlib.pyplot as plt 
import numpy as np
from PIL import Image
from highlight_text import fig_text

from mplsoccer import Bumpy, FontManager, add_image

# font load
font_normal = FontManager('https://raw.githubusercontent.com/googlefonts/roboto/'
                          'main/src/hinted/Roboto-Regular.ttf')
font_bold = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
                        'RobotoSlab[wght].ttf')


# Image data 
epl = Image.open(
    urlopen("https://raw.githubusercontent.com/andrewRowlinson/mplsoccer-assets/main/epl.png")
)

season_dict = json.load(
    urlopen("https://raw.githubusercontent.com/andrewRowlinson/mplsoccer-assets/main/epl.json")
)

player_dict = json.load(
    urlopen("https://raw.githubusercontent.com/andrewRowlinson/mplsoccer-assets/main/"
            "percentile.json")
)

# bumpy_chart는 선 그래프의 특수한 형태 
# 시간 경과에 따른 순위변화를 살펴보는 데 적합, 이 차트를 사용하면 실제 값 
# 자체가 아닌 여러 관측치의 순위, 성과를 서로 쉽게 비교할 수 있음.
# 아래 코드  ex) 19/20 프리미어리그 주간 순위 데이터 

# match-week
match_day = ["Week " + str(num) for num in range(1, 39)]

# highlight dict --> 각 팀마다 해당 색을 나타냄
highlight_dict = {
    "Liverpool": "crimson",
    "Man City": "skyblue",
    "Man Utd": "gold"
}

# 객체 인스턴스화 
# background_color, scatter_color, label_color,line_color 인수를 사용하여
# 플롯의 전체 테마를 변경할 수 있다.
bumpy = Bumpy(
    #background_color="#F6F6F6", scatter_color="#808080",
    scatter_color="#282A2C", line_color="#252525",  # scatter and line colors
    rotate_xticks=90,  # rotate x-ticks by 90 degrees
    ticklabel_size=17, label_size=30,  # ticklable and label font-size
    scatter_primary='D',  # marker to be used
    show_right=True,  # show position on the rightside
    plot_labels=True,  # plot the labels
    alignment_yvalue=0.1,  # y label alignment
    alignment_xvalue=0.065,  # x label alignment
    #scatter_points='D',   # other markers
    
)

# plot bumpy chart
fig, ax = bumpy.plot(
    x_list=match_day,  # match-day or match-week
    y_list=np.linspace(1, 20, 20).astype(int),  # position value from 1 to 20
    values=season_dict,  # values having positions for each team
    secondary_alpha=0.5,   # alpha value for non-shaded lines/markers
    highlight_dict=highlight_dict,  # team to be highlighted with their colors
    figsize=(20, 16),  # size of the figure
    x_label='Week', y_label='Position',  # label name
    ylim=(-0.1, 23),  # y-axis limit
    lw=2.5,   # linewidth of the connecting lines
    # upside_down= True, # Y축 뒤집기
    fontproperties=font_normal.prop,   # fontproperties for ticklables/labels
)

# title and subtitle
TITLE = "Premier League 2019/20 week-wise standings:"
SUB_TITLE = "A comparison between <Liverpool>, <Manchester City> and <Manchester United>"

# add title
fig.text(0.09, 0.95, TITLE, size=29, color="#F2F2F2", fontproperties=font_bold.prop)

# add subtitle
fig_text(
    0.09, 0.94, SUB_TITLE, color="#F2F2F2",
    highlight_textprops=[{"color": 'crimson'}, {"color": 'skyblue'}, {"color": 'gold'}],
    size=25, fig=fig, fontproperties=font_bold.prop
)

# add image
fig = add_image(
     epl,
     fig,  # figure
     0.02, 0.9,  # left and bottom dimensions
     0.08, 0.08  # height and width values
)

# if space is left in the plot use this
plt.tight_layout(pad=0.5)

plt.show()