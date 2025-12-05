import matplotlib.pyplot as plt 
from mplsoccer import Pitch, VerticalPitch


# pitch_color, line_color, stripe_color(stripe= True)를 사용하여 색상 조정
#pitch = Pitch(pitch_type='uefa',
#             pitch_color='#aabb97', line_color='white',
#             stripe_color='#c2d59d', stripe=True)

# pitch_color = 'grass'로 설정하여 잔디 경기장을 표시하기 가능 
pitch = Pitch(pitch_color='grass', line_color='white',
              stripe=True)

fig, ax = pitch.draw()

plt.show()