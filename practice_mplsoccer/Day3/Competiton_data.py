# 액세스 권한이 있는 경우에만 작동합니다
# StatsBomb API로 이동하여 다음을 가정합니다
# 환경을 설정했습니다
# 변수 SB_USERNAME
# 그리고 SB_PASSWARD
# 그렇지 않으면 인수를 통과시킵니다:
# parser = Sbapi(username= 'changeme'),
# password = 'changeme')

#StatsBomb API
#from mplsoccer import Sbapi
#parser = Sbapi(dataframe=True)
#(events, related,
# freeze, tatics) = parser.event(3788741)

#StatsBomb 지역 데이터 
#from mplsoccer import Sblocal
#parser = Sblocal(dataframe=True)
#(events, related,
# freeze, tatics) = parser.event(3788741)

from mplsoccer import Sbopen
parser = Sbopen()

# 경쟁 데이터를 데이터 프레임으로 가져오기 
#df_competition = parser.competition()
#df_competition.info()

# 데이터 일치 
# 매치 데이터를 데이터 프레임으로 가져옵니다. 일부 이벤트 파일에는 오픈 데이터에 매치 데이터가
# 없기 때문에 이 파일의 길이와 팡리 개수가 일치하지 않습니다.
#df_match = parser.match(competition_id=11, season_id=1)
#df_match.info()

# 라인업 데이터 
#df_lineup = parser.lineup(7478)
#df_lineup.info()

# 이벤트 데이터 
#df_event, df_related, df_freeze, df_tactics = parser.event(7478)
#df_event.info()
#df_related.info()
#df_freeze.info()
#df_tactics.info()

# 360 데이터 
df_frame, df_visible = parser.frame(3788741)
df_frame.info()
df_visible.info()