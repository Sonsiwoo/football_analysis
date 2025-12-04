from statsbombpy import sb 
from mplsoccer import Pitch 
import matplotlib.pyplot as plt
import seaborn as sns 

# 1. 데이터 불러오기 (2022 월드컵 결승)
print("데이터를 불러오는 중...(조금 걸릴 수 있음.)")
events = sb.events(match_id=3869685)

# 2. 메시의 모든 터치 데이터 추출(패스, 슈팅, 드리블 등 모든 동작)
# 메시가 공을 건드린 위치를 찾아야 정확환 활동 반경이 나옵니다.
messi_actions = events[events['player']== 'Lionel Andrés Messi Cuccittini'].copy()

# 위치(location)가 비어있는(NaN) 데이터는 제거합니다! (Error 해결)
messi_actions = messi_actions.dropna(subset=['location'])

# 3. 경기장 그리기(이번엔 좀 더 분석적인 스타일)
pitch = Pitch(pitch_type='statsbomb', line_zorder=2, 
              pitch_color='#22312b',line_color='#efefef')
fig, ax = pitch.draw(figsize=(10,7))

# 4. 히트맵(KDE Plot) 그리기 
# fill = True: 색 채우기, levels= 100 : 등고선 디테일 
kde = pitch.kdeplot(
    messi_actions.location.apply(lambda x:x[0]),
    messi_actions.location.apply(lambda x:x[1]),
    ax= ax,
    fill=True,
    levels=100,
    thresh=0.05,  # 너무 옅은 부분은 투명하게(노이즈 제거)
    cmap='hot',   # 색상 테마 (hot: 붉은색 계열)
    alpha=0.8

)

# 5. 제목 달기
plt.title('Lionel Messi - Heatmap (World Cup 2022 Final)', fontsize=20)
plt.show()