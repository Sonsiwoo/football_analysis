import matplotlib.pyplot as plt
from mplsoccer import Pitch, VerticalPitch

plt.xkcd()
pitch = Pitch(pitch_color='grass', stripe=True)
fig, ax = pitch.draw(figsize=(8, 4))
annotation = ax.annotate('Who can resist this?', (60, 10), fontsize=30, ha='center')

plt.show()  # If you are using a Jupyter notebook you do not need this line