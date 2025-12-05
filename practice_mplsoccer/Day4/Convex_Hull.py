from mplsoccer import Pitch, Sbopen
import matplotlib.pyplot as plt 

# read data 
parser = Sbopen()
df, related, freeze, tatics = parser.event(7478)

#Jodie Taylor의 패스 필터링 
df = df[(df.player_name == 'Jodie Taylor') & (df.type_name == 'Pass')].copy()


pitch = Pitch()
fig, ax = pitch.draw(figsize=(8, 6))
hull = pitch.convexhull(df.x, df.y)
poly = pitch.polygon(hull, ax=ax, edgecolor='cornflowerblue', facecolor='cornflowerblue', alpha=0.3)
scatter = pitch.scatter(df.x, df.y, ax=ax, edgecolor='black', facecolor='cornflowerblue')
plt.show() 