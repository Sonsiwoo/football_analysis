import matplotlib.pyplot as plt
from mplsoccer import Pitch, VerticalPitch

pitch= Pitch(pitch_type='uefa')

# tight_layout을 False, constrained_layout을 True
# 보기에 더 깔끔할 수 있음.
fig, ax = pitch.draw(nrows =2, ncols =3, 
                     tight_layout=False,constrained_layout=True)

plt.show()