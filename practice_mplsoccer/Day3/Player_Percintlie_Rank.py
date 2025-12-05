import json 
from urllib.request import urlopen


import matplotlib.pyplot as plt 
import numpy as np
from PIL import Image
from highlight_text import fig_text

from mplsoccer import Bumpy, FontManager, add_image

# 백분위 수 수의 따라 선수 순위 

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

attribute = [
    "xA", "Passes\nInto Pen", "Passes\nInto Final 1/3", "Progressive\nPass Distance",
    "Pass\nReceive%", "Progressive\nCarry Distance"
]
highlight_dict = {
    "Cristián Zapata": "crimson",
    "Francesco Acerbi": "cornflowerblue"
}

# instantiate object
bumpy = Bumpy(
    rotate_xticks=0, ticklabel_size=23, label_size=28, scatter="value",
    show_right=True, alignment_yvalue=0.15, alignment_xvalue=0.06
)

# plot bumpy chart
fig, ax = bumpy.plot(
    x_list=attribute, y_list=np.linspace(1, 100, 11).astype(int), values=player_dict,
    secondary_alpha=0.05, highlight_dict=highlight_dict,
    figsize=(20, 12),
    x_label="Attributes", y_label="Percentile Rank", ylim=(0.5, 12),
    upside_down=True
)

# title and subtitle
TITLE = "Comparison Between <Cristián Zapata> and <Francesco Acerbi>"

# add title
fig_text(
    0.02, 0.98, TITLE, color="#F2F2F2",
    highlight_textprops=[{"color": 'crimson'}, {"color": 'cornflowerblue'}],
    size=34, fig=fig
)
# if space is left in the plot use this
plt.tight_layout(pad=0.5)

plt.show()