import numpy as np 
import pandas as pd 
from matplotlib import animation
from matplotlib import pyplot as plt 
from mplsoccer import Pitch

# Away data 
LINK1 = ('https://raw.githubusercontent.com/metrica-sports/sample-data/master/'
         'data/Sample_Game_1/Sample_Game_1_RawTrackingData_Away_Team.csv')
df_away = pd.read_csv(LINK1, skiprows=2)
df_away.sort_values('Time [s]', inplace=True)

# home data
LINK2 = ('https://raw.githubusercontent.com/metrica-sports/sample-data/master/'
         'data/Sample_Game_1/Sample_Game_1_RawTrackingData_Home_Team.csv')
df_home = pd.read_csv(LINK2, skiprows=2)
df_home.sort_values('Time [s]', inplace=True)


# 열 이름 재설정 
def set_col_names(df):
    """ Renames the columns to have x and y suffixes."""
    cols = list(np.repeat(df.columns[3::2], 2))
    cols = [col+'_x' if i % 2 == 0 else col+'_y' for i, col in enumerate(cols)]
    cols = np.concatenate([df.columns[:3], cols])
    df.columns = cols


set_col_names(df_away)
set_col_names(df_home)

# 2초 분량의 데이터 
df_away = df_away[(df_away['Time [s]'] >= 815) & (df_away['Time [s]'] < 825)].copy()
df_home = df_home[(df_home['Time [s]'] >= 815) & (df_home['Time [s]'] < 825)].copy()


# 볼 데이터를 분할하고 df_away/ df_home 데이터 프레임에서 볼 열을 삭제
df_ball = df_away[['Period', 'Frame', 'Time [s]', 'Ball_x', 'Ball_y']].copy()
df_home.drop(['Ball_x', 'Ball_y'], axis=1, inplace=True)
df_away.drop(['Ball_x', 'Ball_y'], axis=1, inplace=True)
df_ball.rename({'Ball_x': 'x', 'Ball_y': 'y'}, axis=1, inplace=True)

# 넓은 형태에서 긴 형태로 변환 
def to_long_form(df):
    """ Pivots a dataframe from wide-form (each player as a separate column) to long form (rows)"""
    df = pd.melt(df, id_vars=df.columns[:3], value_vars=df.columns[3:], var_name='player')
    df.loc[df.player.str.contains('_x'), 'coordinate'] = 'x'
    df.loc[df.player.str.contains('_y'), 'coordinate'] = 'y'
    df = df.dropna(axis=0, how='any')
    df['player'] = df.player.str[6:-2]
    df = (df.set_index(['Period', 'Frame', 'Time [s]', 'player', 'coordinate'])['value']
          .unstack()
          .reset_index()
          .rename_axis(None, axis=1))
    return df


df_away = to_long_form(df_away)
df_home = to_long_form(df_home)

# 원정 데이터 표시
df_away.head()
# 홈 데이터 표시 
df_home.head()
# ball 데이터 표시 
df_ball.head()

# 첫 번째 도형을 설정하고 축을 설정 
pitch = Pitch(pitch_type='metricasports',pitch_color='grass',
              line_color='white',
              goal_type='line',pitch_width=68,
              pitch_length=105,)
fig, ax = pitch.draw(figsize=(16, 10.4))

# 애니메이션할 피치 플롯 마커를 설정합니다
marker_kwargs = {'marker': 'o', 'markeredgecolor': 'black', 'linestyle': 'None'}
ball, = ax.plot([], [], ms=6, markerfacecolor='w', zorder=3, **marker_kwargs)
away, = ax.plot([], [], ms=10, markerfacecolor='#b94b75', **marker_kwargs)  # red/maroon
home, = ax.plot([], [], ms=10, markerfacecolor='#7f63b8', **marker_kwargs)  # purple


# 애니메이션 함수
def animate(i):
    """ 데이터를 애니메이션화하는 기능. 각 프레임은 플레이어와 공의 데이터를 설정합니다."""
    # i번째 프레임의 x와 y 위치로 볼 데이터 설정
    ball.set_data(df_ball.iloc[i, [3]], df_ball.iloc[i, [4]])
    # i번째 프레임의 프레임 ID 가져오기
    frame = df_ball.iloc[i, 1]
    # 프레임 ID를 사용하여 플레이어 데이터 설정
    away.set_data(df_away.loc[df_away.Frame == frame, 'x'],
                  df_away.loc[df_away.Frame == frame, 'y'])
    home.set_data(df_home.loc[df_home.Frame == frame, 'x'],
                  df_home.loc[df_home.Frame == frame, 'y'])
    return ball, away, home


# 애니메이터에게 call 초당 25프레임으로 애니메이터 만들기
anim = animation.FuncAnimation(fig, animate, frames=len(df_ball), interval=50, blit=True)
plt.show()

# fffmpeg 요구 사항을 제대로 파악하기 어렵다는 점을 유의하세요.
# conda-forge에서 설치했습니다: 문서 폴더에 있는 environment.yml 파일을 참조하세요
# 애니메이션을 저장하는 방법 - 예를 들어 댓글 달기
# anim.save ('example.mp4', dpi=150, fps=25,
# extra_args=[-vcodec], 'libx264'],
# savefig_kwargs={'pad_inches':0, '얼굴색':'#457E29'}