import pandas as pd
from statsbombpy import sb
from mplsoccer import Pitch
import matplotlib.pyplot as plt
import warnings

# 경고 메시지 무시
warnings.filterwarnings('ignore')

def fetch_match_events(match_id):
    """
    특정 경기(match_id)의 모든 이벤트 데이터를 가져오는 함수
    """
    print(f"Loading data for Match ID: {match_id}...")
    events = sb.events(match_id=match_id)
    return events

def draw_pass_map(events, team_name, player_name):
    """
    특정 선수(player_name)의 패스 맵을 그리는 함수
    """
    # 1. 데이터 필터링 (팀 -> 선수 -> 패스)
    team_events = events[events['team'] == team_name]
    player_events = team_events[team_events['player'] == player_name]
    passes = player_events[player_events['type'] == 'Pass']
    
    print(f"{player_name}의 총 패스 시도: {len(passes)}회")

    # 2. 피치 생성
    pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc')
    fig, ax = pitch.draw(figsize=(12, 8))

    # 3. 성공/실패 패스 분리
    pass_completed = passes[passes['pass_outcome'].isnull()]
    pass_failed = passes[passes['pass_outcome'].notnull()]

    # 4. 화살표 그리기 (성공=초록, 실패=빨강)
    # 성공 패스
    pitch.arrows(pass_completed.location.apply(lambda x: x[0]), 
                 pass_completed.location.apply(lambda x: x[1]),
                 pass_completed.pass_end_location.apply(lambda x: x[0]), 
                 pass_completed.pass_end_location.apply(lambda x: x[1]),
                 ax=ax, color='green', width=2, headwidth=3, label='Completed')
    
    # 실패 패스
    pitch.arrows(pass_failed.location.apply(lambda x: x[0]), 
                 pass_failed.location.apply(lambda x: x[1]),
                 pass_failed.pass_end_location.apply(lambda x: x[0]), 
                 pass_failed.pass_end_location.apply(lambda x: x[1]),
                 ax=ax, color='red', width=2, headwidth=3, label='Failed')

    # 5. 타이틀 및 출력
    ax.set_title(f'{player_name} Pass Map (vs France)', fontsize=20, color='white')
    plt.legend(facecolor='white', handlelength=3, edgecolor='none', fontsize=12, loc='upper left')
    plt.show()

# 메인 실행 블록
if __name__ == "__main__":
    # 2022 월드컵 결승전 ID
    MATCH_ID = 3869685
    
    # 데이터 로딩
    match_events = fetch_match_events(MATCH_ID)
    
    # 메시 패스 맵 그리기
    draw_pass_map(match_events, 'Argentina', 'Lionel Andrés Messi Cuccittini')