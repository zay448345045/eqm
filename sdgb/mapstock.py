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
                "mapStock": 99000,
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
        "userItemList": [],
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
        "isNewItemList": "",
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
