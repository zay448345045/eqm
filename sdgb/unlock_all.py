import json
import pytz
import time
import random

from sdgb import sdgb_api
from datetime import datetime, timedelta

from settings import userId
from settings import music_data
from settings import regionId, clientId, placeId, regionName, placeName

from login import login
from logout import logout

def CalcRandom():
    max = 1037933
    num2 = random.randint(1, max) * 2069

    num2 += 1024  # specialnum
    num3 = 0
    for i in range(0, 32):
        num3 <<= 1
        num3 += num2 % 2
        num2 >>= 1

    return num3

timestamp = int(time.time()) - 60

def music():

    music = music_data

    musicId = music['musicId']
    level = music['level']
    playCount = music['playCount']
    achievement = music['achievement']
    comboStatus = music['comboStatus']
    syncStatus = music['syncStatus']
    deluxscoreMax = music['deluxscoreMax']
    scoreRank = music['scoreRank']
    extNum1 = music['extNum1']

    print(timestamp)

    # UserLogin

    login_result = json.loads(login(timestamp))
    print(login_result)

    login_id = login_result['loginId']
    login_date = login_result['lastLoginDate']


    # UserData

    data = json.dumps({
        "userId": int(userId)
    })

    userdata = json.loads(sdgb_api(data, "GetUserDataApi", userId))

    # UserLog

    data = json.dumps({
    "userId": int(userId),
    "userPlaylog": {
        "userId": 0,
        "orderId": 0,
        "playlogId": login_id,
        "version": 1041000,
        "placeId": placeId,
        "placeName": placeName,
        "loginDate": int(time.time()),
        "playDate": datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d'),
        "userPlayDate": datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S') + '.0',
        "type": 0,
        "musicId": int(musicId),
        "level": int(level),
        "trackNo": 1,
        "vsMode": 0,
        "vsUserName": "",
        "vsStatus": 0,
        "vsUserRating": 0,
        "vsUserAchievement": 0,
        "vsUserGradeRank": 0,
        "vsRank": 0,
        "playerNum": 1,
        "playedUserId1": 0,
        "playedUserName1": "",
        "playedMusicLevel1": 0,
        "playedUserId2": 0,
        "playedUserName2": "",
        "playedMusicLevel2": 0,
        "playedUserId3": 0,
        "playedUserName3": "",
        "playedMusicLevel3": 0,
        "characterId1": userdata['userData']['charaSlot'][0],
        "characterLevel1": random.randint(1000,6500),
        "characterAwakening1": 5,
        "characterId2": userdata['userData']['charaSlot'][1],
        "characterLevel2": random.randint(1000,6500),
        "characterAwakening2": 5,
        "characterId3": userdata['userData']['charaSlot'][2],
        "characterLevel3": random.randint(1000,6500),
        "characterAwakening3": 5,
        "characterId4": userdata['userData']['charaSlot'][3],
        "characterLevel4": random.randint(1000,6500),
        "characterAwakening4": 5,
        "characterId5": userdata['userData']['charaSlot'][4],
        "characterLevel5": random.randint(1000,6500),
        "characterAwakening5": 5,
        "achievement": int(achievement),
        "deluxscore": int(deluxscoreMax),
        "scoreRank": int(scoreRank),
        "maxCombo": random.randint(400,500),
        "totalCombo": random.randint(700,900),
        "maxSync": 0,
        "totalSync": 0,
        "tapCriticalPerfect": random.randint(200,400),
        "tapPerfect": random.randint(100,250),
        "tapGreat": random.randint(0,10),
        "tapGood": random.randint(0,10),
        "tapMiss": random.randint(0,10),
        "holdCriticalPerfect": random.randint(20,40),
        "holdPerfect": random.randint(0,15),
        "holdGreat": 0,
        "holdGood": 0,
        "holdMiss": 0,
        "slideCriticalPerfect": random.randint(34,60),
        "slidePerfect": 0,
        "slideGreat": 0,
        "slideGood": 0,
        "slideMiss": 0,
        "touchCriticalPerfect": random.randint(20,70),
        "touchPerfect": 0,
        "touchGreat": 0,
        "touchGood": 0,
        "touchMiss": 0,
        "breakCriticalPerfect": random.randint(8,30),
        "breakPerfect": random.randint(7,10),
        "breakGreat": 0,
        "breakGood": 0,
        "breakMiss": 0,
        "isTap": True,
        "isHold": True,
        "isSlide": True,
        "isTouch": True,
        "isBreak": True,
        "isCriticalDisp": True,
        "isFastLateDisp": True,
        "fastCount": random.randint(20,30),
        "lateCount": random.randint(50,70),
        "isAchieveNewRecord": True,
        "isDeluxscoreNewRecord": True,
        "comboStatus": 0,
        "syncStatus": 0,
        "isClear": True,
        'beforeRating': userdata['userData']['playerRating'],
        'afterRating': userdata['userData']['playerRating'],
        "beforeGrade": 0,
        "afterGrade": 0,
        "afterGradeRank": 2,
        'beforeDeluxRating': userdata['userData']['playerRating'],
        'afterDeluxRating': userdata['userData']['playerRating'],
        "isPlayTutorial": False,
        "isEventMode": False,
        "isFreedomMode": False,
        "playMode": 0,
        "isNewFree": False,
        "trialPlayAchievement": -1,
        "extNum1": 0,
        "extNum2": 0,
        "extNum4": 3020,
        "extBool1": False
        }
    })

    userlog_result = json.loads(sdgb_api(data, "UploadUserPlaylogApi", userId))

    print(userlog_result)


    # 获取 User Extend
    data = json.dumps({
        "userId": int(userId)
    })

    user_extend = json.loads(sdgb_api(data, "GetUserExtendApi", userId))

    # 获取 User Option
    data = json.dumps({
        "userId": int(userId)
    })

    user_option = json.loads(sdgb_api(data, "GetUserOptionApi", userId))
    

    # 获取 User Rating
    data = json.dumps({
        "userId": int(userId)
    })

    user_rating = json.loads(sdgb_api(data, "GetUserRatingApi", userId))
    

    # 获取 User Activity
    data = json.dumps({
        "userId": int(userId)
    })

    user_activity = json.loads(sdgb_api(data, "GetUserActivityApi", userId))
    

    # 获取账号功能票
    data = json.dumps({
        "userId": int(userId)
    })

    user_charge = json.loads(sdgb_api(data, "GetUserChargeApi", userId))




    # UserAll

    data = json.dumps({
    "userId": int(userId),
    "playlogId": login_id,
    "isEventMode": False,
    "isFreePlay": False,
    "upsertUserAll": {
        "userData": [
            {
                "accessCode": "",
                "userName": userdata['userData']['userName'],
                "isNetMember": 1,
                "iconId": userdata['userData']['iconId'],
                "plateId": userdata['userData']['plateId'],
                "titleId": userdata['userData']['titleId'],
                "partnerId": userdata['userData']['partnerId'],
                "frameId": userdata['userData']['frameId'],
                "selectMapId": userdata['userData']['selectMapId'],
                "totalAwake": userdata['userData']['totalAwake'],
                "gradeRating": userdata['userData']['gradeRating'],
                "musicRating": userdata['userData']['musicRating'],
                "playerRating": userdata['userData']['playerRating'],
                "highestRating": userdata['userData']['highestRating'],
                "gradeRank": userdata['userData']['gradeRank'],
                "classRank": userdata['userData']['classRank'],
                "courseRank": userdata['userData']['courseRank'],
                "charaSlot": userdata['userData']['charaSlot'],
                "charaLockSlot": userdata['userData']['charaLockSlot'],
                "contentBit": userdata['userData']['contentBit'],
                "playCount": userdata['userData']['playCount'],
                "currentPlayCount": userdata['userData']['currentPlayCount'],
                "renameCredit": 0,
                "mapStock": userdata['userData']['mapStock'],
                "eventWatchedDate": userdata['userData']['eventWatchedDate'],
                "lastGameId": "SDGB",
                "lastRomVersion": userdata['userData']['lastRomVersion'],
                "lastDataVersion": userdata['userData']['lastDataVersion'],
                "lastLoginDate": login_date,
                "lastPlayDate": datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S') + '.0',
                "lastPlayCredit": 1,
                "lastPlayMode": 0,
                "lastPlaceId": placeId,
                "lastPlaceName": placeName,
                "lastAllNetId": 0,
                "lastRegionId": regionId,
                "lastRegionName": regionName,
                "lastClientId": clientId,
                "lastCountryCode": "CHN",
                "lastSelectEMoney": 0,
                "lastSelectTicket": 0,
                "lastSelectCourse": userdata['userData']['lastSelectCourse'],
                "lastCountCourse": 0,
                "firstGameId": "SDGB",
                "firstRomVersion": userdata['userData']['firstRomVersion'],
                "firstDataVersion": userdata['userData']['firstDataVersion'],
                "firstPlayDate": userdata['userData']['firstPlayDate'],
                "compatibleCmVersion": userdata['userData']['compatibleCmVersion'],
                "dailyBonusDate": userdata['userData']['dailyBonusDate'],
                "dailyCourseBonusDate": userdata['userData']['dailyCourseBonusDate'],
                "lastPairLoginDate": userdata['userData']['lastPairLoginDate'],
                "lastTrialPlayDate": userdata['userData']['lastTrialPlayDate'],
                "playVsCount": 0,
                "playSyncCount": 0,
                "winCount": 0,
                "helpCount": 0,
                "comboCount": 0,
                "totalDeluxscore": userdata['userData']['totalDeluxscore'],
                "totalBasicDeluxscore": userdata['userData']['totalBasicDeluxscore'],
                "totalAdvancedDeluxscore": userdata['userData']['totalAdvancedDeluxscore'],
                "totalExpertDeluxscore": userdata['userData']['totalExpertDeluxscore'],
                "totalMasterDeluxscore": userdata['userData']['totalMasterDeluxscore'],
                "totalReMasterDeluxscore": userdata['userData']['totalReMasterDeluxscore'],
                "totalSync": userdata['userData']['totalSync'],
                "totalBasicSync": userdata['userData']['totalBasicSync'],
                "totalAdvancedSync": userdata['userData']['totalAdvancedSync'],
                "totalExpertSync": userdata['userData']['totalExpertSync'],
                "totalMasterSync": userdata['userData']['totalMasterSync'],
                "totalReMasterSync": userdata['userData']['totalReMasterSync'],
                "totalAchievement": userdata['userData']['totalAchievement'],
                "totalBasicAchievement": userdata['userData']['totalBasicAchievement'],
                "totalAdvancedAchievement": userdata['userData']['totalAdvancedAchievement'],
                "totalExpertAchievement": userdata['userData']['totalExpertAchievement'],
                "totalMasterAchievement": userdata['userData']['totalMasterAchievement'],
                "totalReMasterAchievement": userdata['userData']['totalReMasterAchievement'],
                "playerOldRating": userdata['userData']['playerOldRating'],
                "playerNewRating": userdata['userData']['playerNewRating'],
                "banState": 0,
                "dateTime": timestamp
            }
        ],
        "userExtend": [user_extend['userExtend']],
        "userOption": [user_option['userOption']],
        "userCharacterList": [],
        "userGhost": [],
        "userMapList": [],
        "userLoginBonusList": [],
        "userRatingList": [user_rating['userRating']],
        "userItemList": [
{
    "itemKind": 5,
    "itemId": 11001,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11002,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11003,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11004,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11005,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11006,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11007,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11008,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11009,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11010,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11014,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11015,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11016,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11017,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11018,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11019,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11020,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11021,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11022,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11023,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11024,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11025,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11026,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11027,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11028,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11029,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11030,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11031,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11032,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11034,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11037,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11043,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11044,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11046,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11048,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11049,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11050,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11051,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11052,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11058,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11059,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11060,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11061,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11064,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11065,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11066,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11067,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11069,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11070,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11073,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11075,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11077,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11078,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11080,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11081,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11083,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11084,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11085,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11086,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11087,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11088,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11089,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11090,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11091,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11092,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11093,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11094,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11095,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11096,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11097,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11098,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11099,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11100,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11101,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11102,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11103,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11104,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11105,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11106,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11107,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11108,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11109,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11110,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11111,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11113,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11115,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11121,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11122,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11123,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11124,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11125,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11126,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11127,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11128,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11129,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11130,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11131,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11132,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11133,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11134,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11135,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11136,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11137,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11138,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11139,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11140,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11141,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11142,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11143,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11150,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11152,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11153,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11154,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11155,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11157,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11158,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11159,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11160,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11161,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11162,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11163,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11164,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11165,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11166,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11167,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11168,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11169,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11170,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11171,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11172,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11173,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11174,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11175,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11176,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11177,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11184,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11185,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11186,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11187,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11188,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11189,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11190,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11191,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11192,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11193,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11194,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11195,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11198,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11199,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11200,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11201,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11202,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11204,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11205,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11206,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11207,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11208,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11209,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11210,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11211,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11212,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11213,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11214,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11215,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11216,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11219,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11221,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11222,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11223,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11224,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11225,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11226,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11227,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11228,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11229,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11230,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11231,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11232,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11233,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11234,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11235,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11236,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11237,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11238,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11239,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11240,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11241,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11242,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11243,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11246,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11247,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11248,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11249,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11253,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11255,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11260,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11261,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11262,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11263,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11264,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11265,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11266,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11267,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11268,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11269,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11270,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11271,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11272,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11273,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11274,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11275,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11276,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11277,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11278,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11279,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11280,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11281,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11282,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11283,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11284,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11285,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11286,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11287,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11288,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11289,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11290,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11291,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11292,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11293,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11294,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11295,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11296,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11297,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11298,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11299,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11300,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11301,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11302,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11303,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11304,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11305,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11306,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11307,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11308,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11309,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11310,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11311,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11312,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11313,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11314,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11315,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11316,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11317,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11318,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11319,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11321,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11322,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11323,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11324,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11325,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11327,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11328,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11330,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11331,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11333,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11334,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11335,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11336,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11340,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11341,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11342,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11343,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11344,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11345,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11346,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11347,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11348,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11349,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11350,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11351,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11353,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11354,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11355,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11358,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11359,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11360,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11361,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11362,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11363,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11364,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11365,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11367,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11369,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11370,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11373,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11374,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11375,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11376,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11377,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11378,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11379,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11380,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11381,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11382,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11383,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11384,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11385,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11386,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11387,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11388,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11389,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11390,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11391,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11392,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11393,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11394,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11395,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11396,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11398,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11399,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11400,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11401,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11402,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11404,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11405,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11407,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11408,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11410,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11411,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11412,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11413,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11415,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11418,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11419,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11420,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11421,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11422,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11423,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11424,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11425,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11426,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11427,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11428,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11429,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11430,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11431,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11432,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11433,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11434,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11435,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11436,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11437,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11438,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11439,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11441,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11443,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11444,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11445,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11446,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11447,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11448,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11449,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11450,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11451,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11452,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11453,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11454,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11455,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11456,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11457,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11458,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11459,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11460,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11461,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11462,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11463,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11464,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11465,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11466,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11467,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11468,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11469,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11470,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11471,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11472,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11473,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11474,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11475,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11477,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11478,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11479,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11481,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11482,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11483,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11484,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11485,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11486,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11487,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11488,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11489,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11490,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11491,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11495,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11496,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11497,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11498,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11499,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11500,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11502,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11503,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11504,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11505,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11506,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11507,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11508,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11509,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11510,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11511,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11512,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11513,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11514,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11516,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11517,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11518,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11519,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11520,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11521,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11523,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11524,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11525,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11526,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11527,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11528,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11529,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11530,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11532,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11533,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11534,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11535,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11536,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11537,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11538,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11539,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11540,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11541,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11542,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11543,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11544,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11545,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11546,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11547,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11548,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11549,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11550,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11551,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11552,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11553,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11554,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11555,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11556,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11557,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11558,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11559,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11560,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11561,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11562,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11563,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11564,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11565,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11566,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11567,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11568,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11569,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11570,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11571,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11572,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11573,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11574,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11575,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11576,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11577,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11578,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11580,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11583,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11584,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11585,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11586,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11587,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11588,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11589,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11590,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11591,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11592,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11593,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11594,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11596,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11597,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11598,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11599,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11600,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11601,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11602,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11603,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11604,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11605,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11606,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11607,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11608,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11609,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11610,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11611,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11612,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11613,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11614,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11615,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11616,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11617,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11618,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11619,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11620,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11621,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11622,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11623,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11624,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11625,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11626,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11627,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11628,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11629,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11630,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11631,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11632,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11633,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11635,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11636,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11637,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11638,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11639,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11640,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11641,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11642,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11643,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11645,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11646,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11647,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11648,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11650,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11651,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11652,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11653,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11654,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11655,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11656,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11657,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11658,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11659,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11660,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11661,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11662,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11663,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11664,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 11668,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11001,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11002,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11003,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11004,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11005,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11006,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11007,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11008,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11009,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11010,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11014,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11015,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11016,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11017,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11018,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11019,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11020,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11021,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11022,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11023,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11024,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11025,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11026,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11027,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11028,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11029,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11030,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11031,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11032,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11034,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11037,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11043,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11044,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11046,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11048,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11049,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11050,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11051,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11052,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11058,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11059,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11060,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11061,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11064,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11065,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11066,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11067,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11069,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11070,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11073,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11075,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11077,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11078,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11080,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11081,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11083,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11084,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11085,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11086,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11087,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11088,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11089,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11090,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11091,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11092,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11093,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11094,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11095,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11096,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11097,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11098,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11099,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11100,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11101,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11102,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11103,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11104,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11105,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11106,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11107,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11108,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11109,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11110,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11111,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11113,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11115,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11121,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11122,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11123,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11124,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11125,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11126,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11127,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11128,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11129,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11130,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11131,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11132,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11133,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11134,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11135,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11136,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11137,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11138,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11139,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11140,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11141,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11142,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11143,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11150,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11152,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11153,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11154,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11155,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11157,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11158,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11159,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11160,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11161,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11162,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11163,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11164,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11165,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11166,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11167,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11168,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11169,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11170,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11171,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11172,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11173,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11174,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11175,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11176,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11177,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11184,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11185,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11186,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11187,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11188,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11189,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11190,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11191,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11192,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11193,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11194,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11195,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11198,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11199,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11200,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11201,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11202,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11204,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11205,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11206,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11207,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11208,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11209,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11210,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11211,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11212,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11213,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11214,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11215,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11216,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11219,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11221,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11222,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11223,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11224,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11225,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11226,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11227,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11228,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11229,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11230,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11231,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11232,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11233,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11234,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11235,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11236,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11237,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11238,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11239,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11240,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11241,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11242,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11243,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11246,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11247,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11248,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11249,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11253,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11255,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11260,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11261,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11262,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11263,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11264,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11265,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11266,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11267,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11268,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11269,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11270,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11271,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11272,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11273,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11274,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11275,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11276,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11277,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11278,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11279,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11280,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11281,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11282,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11283,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11284,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11285,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11286,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11287,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11288,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11289,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11290,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11291,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11292,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11293,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11294,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11295,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11296,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11297,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11298,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11299,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11300,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11301,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11302,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11303,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11304,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11305,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11306,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11307,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11308,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11309,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11310,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11311,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11312,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11313,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11314,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11315,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11316,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11317,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11318,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11319,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11321,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11322,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11323,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11324,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11325,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11327,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11328,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11330,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11331,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11333,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11334,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11335,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11336,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11340,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11341,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11342,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11343,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11344,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11345,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11346,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11347,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11348,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11349,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11350,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11351,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11353,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11354,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11355,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11358,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11359,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11360,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11361,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11362,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11363,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11364,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11365,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11367,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11369,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11370,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11373,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11374,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11375,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11376,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11377,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11378,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11379,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11380,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11381,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11382,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11383,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11384,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11385,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11386,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11387,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11388,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11389,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11390,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11391,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11392,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11393,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11394,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11395,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11396,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11398,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11399,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11400,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11401,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11402,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11404,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11405,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11407,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11408,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11410,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11411,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11412,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11413,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11415,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11418,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11419,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11420,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11421,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11422,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11423,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11424,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11425,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11426,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11427,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11428,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11429,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11430,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11431,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11432,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11433,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11434,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11435,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11436,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11437,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11438,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11439,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11441,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11443,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11444,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11445,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11446,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11447,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11448,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11449,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11450,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11451,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11452,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11453,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11454,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11455,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11456,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11457,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11458,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11459,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11460,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11461,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11462,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11463,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11464,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11465,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11466,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11467,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11468,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11469,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11470,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11471,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11472,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11473,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11474,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11475,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11477,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11478,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11479,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11481,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11482,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11483,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11484,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11485,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11486,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11487,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11488,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11489,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11490,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11491,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11495,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11496,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11497,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11498,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11499,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11500,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11502,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11503,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11504,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11505,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11506,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11507,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11508,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11509,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11510,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11511,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11512,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11513,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11514,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11516,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11517,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11518,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11519,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11520,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11521,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11523,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11524,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11525,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11526,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11527,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11528,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11529,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11530,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11532,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11533,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11534,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11535,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11536,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11537,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11538,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11539,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11540,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11541,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11542,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11543,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11544,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11545,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11546,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11547,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11548,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11549,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11550,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11551,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11552,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11553,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11554,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11555,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11556,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11557,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11558,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11559,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11560,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11561,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11562,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11563,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11564,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11565,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11566,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11567,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11568,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11569,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11570,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11571,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11572,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11573,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11574,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11575,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11576,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11577,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11578,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11580,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11583,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11584,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11585,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11586,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11587,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11588,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11589,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11590,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11591,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11592,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11593,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11594,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11596,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11597,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11598,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11599,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11600,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11601,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11602,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11603,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11604,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11605,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11606,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11607,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11608,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11609,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11610,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11611,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11612,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11613,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11614,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11615,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11616,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11617,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11618,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11619,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11620,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11621,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11622,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11623,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11624,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11625,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11626,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11627,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11628,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11629,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11630,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11631,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11632,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11633,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11635,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11636,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11637,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11638,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11639,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11640,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11641,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11642,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11643,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11645,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11646,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11647,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11648,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11650,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11651,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11652,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11653,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11654,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11655,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11656,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11657,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11658,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11659,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11660,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11661,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11662,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11663,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11664,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 11668,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10070,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10145,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10146,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10188,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10190,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10191,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10193,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10202,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10235,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10256,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10288,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10301,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10302,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10315,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10316,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10319,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10363,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10404,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10420,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10536,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10552,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10572,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10593,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10602,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10625,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10641,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10665,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10690,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10702,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10706,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 5,
    "itemId": 10734,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10070,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10145,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10146,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10188,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10190,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10191,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10193,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10202,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10235,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10256,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10288,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10301,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10302,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10315,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10316,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10319,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10363,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10404,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10420,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10536,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10552,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10572,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10593,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10602,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10625,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10641,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10665,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10690,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10702,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10706,
    "stock": 1,
    "isValid": True
},
{
    "itemKind": 6,
    "itemId": 10734,
    "stock": 1,
    "isValid": True
}
        ],
        "userMusicDetailList": [
            {
                "musicId": musicId,
                "level": level,
                "playCount": playCount,
                "achievement": achievement,
                "comboStatus": comboStatus,
                "syncStatus": syncStatus,
                "deluxscoreMax": deluxscoreMax,
                "scoreRank": scoreRank,
                "extNum1": extNum1
            }
        ],
        "userCourseList": [],
        "userFriendSeasonRankingList": [],
        "userChargeList": user_charge['userChargeList'],
        "userFavoriteList": [],
        "userActivityList": [user_activity['userActivity']],
        "userGamePlaylogList": [
            {
                "playlogId": login_id,
                "version": "1.41.00",
                "playDate": datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S') + '.0',
                "playMode": 0,
                "useTicketId": -1,
                "playCredit": 1,
                "playTrack": 1,
                "clientId": clientId,
                "isPlayTutorial": False,
                "isEventMode": False,
                "isNewFree": False,
                "playCount": 0,
                "playSpecial": CalcRandom(),
                "playOtherUserId": 0
            }
        ],
        "user2pPlaylog": {
            "userId1": 0,
            "userId2": 0,
            "userName1": "",
            "userName2": "",
            "regionId": 0,
            "placeId": 0,
            "user2pPlaylogDetailList": []
        },
        "isNewCharacterList": "",
        "isNewMapList": "",
        "isNewLoginBonusList": "",
        "isNewItemList": 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
        "isNewMusicDetailList": "1",
        "isNewCourseList": "0",
        "isNewFavoriteList": "",
        "isNewFriendSeasonRankingList": ""
        }
    })

    userall_result = json.loads(sdgb_api(data, "UpsertUserAllApi", userId))
    return userall_result

def music_with_retry(max_retries=10): # 这里是重试次数
    for i in range(max_retries):
        try:
            print(music())
            return logout(timestamp)
        except ValueError as e:
            print(f"尝试 {i+1} 失败，错误：{e}")
            print(logout(timestamp))
            time.sleep(5)  # 等待 5 秒后重试
    return "重试次数超过限制，乐曲上传失败"

if __name__ == "__main__":
    print(music_with_retry())
