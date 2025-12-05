import matplotlib.pyplot as plt
from mplsoccer import Pitch, VerticalPitch

# 수평 전체 
# pitch = Pitch(half=False)

# 수평 절반 
# pitch = Pitch(half = True)

# 수직 절반 
# pitch = VerticalPitch(half=True)

# pad_left 또한, pad_right, 인수 pad_bottom를 사용하여 
# 피치 방향을 조절하여 pad_top 임의의 피치 모양을 만들 수 있습니다.
pitch = VerticalPitch(half=True,
                      pad_left=10,
                      pad_right=10,
                      pad_top=10,
                      pad_bottom=20)

fig, ax = pitch.draw()

plt.show()