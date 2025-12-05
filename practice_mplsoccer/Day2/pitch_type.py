import pprint
import matplotlib.pyplot as plt
from mplsoccer import Pitch
from mplsoccer.soccer.dimensions import valid
pprint.pp(valid)

# 기본 피치는 StatsBomb, x축 제한은 0~120이고 y축 제한은 80~0(반전)
# pitch = Pitch(pitch_type='statsbomb', axis=True,label=True)

# Tracab은 데이터 추적을 위한 중심 Pitch 
# pitch = Pitch(pitch_type='tracab', pitch_width=68, pitch_length=105,
#             axis=True, label=True)


# Stats Perform의 Opta 데이터엔은 0과 100 사이의 x,y 제한이 모두 있음.
#opta 피치 좌표는 sofascore와 WhoScored에서 사용 
pitch = Pitch(pitch_type='opta', axis=True,label=True)

# Wyscout: y축 반전 
# pitch = Pitch(pitch_type='wyscout', axis=True, label=True)

# UEFA 경기장은 경기장 길이와 경기장 너비가 UEFA 표준(105m * 65m)으로 
# 설정된 맞춤형 경기장의 특수한 경우입니다.
# pitch = Pitch(pitch_type='uefa', axis=True, label=True)

fig, ax = pitch.draw()

plt.show()