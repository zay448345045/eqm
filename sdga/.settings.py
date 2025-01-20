# This file contains the config of the whole project.
# DO NOT share your crtical info to others.
# Change the file name from .settings.py to settings.py.
from sdgb import aimedb_api, felica

accessCode = 50000000000000000000
IDm = "0000000000000000"

felica(IDm)

userId = aimedb_api(accessCode)

# 上传的乐曲成绩
# 此成绩将覆盖原有成绩

music_data = ({
    "musicId": 11588,
    "level": 3,
    "playCount": 11,
    "achievement": 1005627,
    "comboStatus": 0,
    "syncStatus": 0,
    "deluxscoreMax": 2362,
    "scoreRank": 13,
    "extNum1": 0
})

# 机厅信息

regionId = 114
regionName = "Yau Tsim Mong"
placeId = 6412
placeName = "GOLDEN ERA GAME CENTRE"
clientId = "A63E01E0048"
