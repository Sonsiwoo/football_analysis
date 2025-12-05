import matplotlib.pyplot as plt
from mplsoccer import Pitch, VerticalPitch

# mplsoccer는 pitch_type 'statsbomb', 'opta','uefa'와 같은 
# 10가지 구장을 유형을 지원 
pitch = Pitch(pitch_type='opta')  
fig, ax = pitch.draw()

plt.show()