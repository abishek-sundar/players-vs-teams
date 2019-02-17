# import nba_api.stats.endpoints as nba_st_end
# import nba_api as nba
# pbp = nba_st_end.playbyplay.PlayByPlay('0021701171')
# pbp = pbp.get_data_frames()[0]
# print (pbp)
from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import playbyplayv2
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playergamelog

playerid = players.find_players_by_full_name('Damian Lillard')[0]['id']
gamefinder = leaguegamefinder.LeagueGameFinder(player_id_nullable = playerid)
plays_for = commonplayerinfo.CommonPlayerInfo(player_id=playerid).get_data_frames()[0].at[0,'TEAM_ABBREVIATION']
score = playergamelog.PlayerGameLog(season_all = "ALL", player_id = playerid)

againstTeam = {}
for team in teams.get_teams():
    againstTeam[team['abbreviation']] = 0
for i in range(len(games.index)):
    print(i)
    pbp = playbyplayv2.PlayByPlayV2(games.at[i,'GAME_ID'])
    pbp = pbp.get_data_frames()[0]
    match = games.at[i,'MATCHUP']

    if ("@ " + plays_for in match) or (plays_for + " vs." in match):
        home = True
    else:
        home = False

    if home:
        if "@" not in match:
            awayTeam = match.split()[2]
        else:
            awayTeam = match.split()[0]

    else:
        if "@" in match:
            awayTeam = match.split()[2]
        else:
            awayTeam = match.split()[0]
    pbp = pbp[pbp.PLAYER1_ID == playerid]
    pbp = pbp[pbp.EVENTMSGTYPE == 1]
    for j in range(len(pbp.index)): #eventmsg == 1
        if (home):
            desc = pbp.iloc[j]["HOMEDESCRIPTION"]
        else:
            desc = pbp.iloc[j]["VISITORDESCRIPTION"]
        descsplit=desc.split()
        feet = descsplit[1][0:(len(descsplit[1])-1)]
        feet = float(feet) 
        if (feet>againstTeam[awayTeam]):
            againstTeam[awayTeam] =feet
        
print (againstTeam)
#["0021700807",25,1,1,1,"8:13 PM","9:28",null,null,"Wiggins 27' 3PT Jump Shot (5 PTS) (Butler 1 AST)","7 - 5","-2",5,203952,"Andrew Wiggins",1610612750,"Minnesota","Timberwolves","MIN",5,202710,"Jimmy Butler",1610612750,"Minnesota","Timberwolves","MIN",0,0,null,null,null,null,null]