import json

from sdgb import sdgb_api

def login(userId):
    data = json.dumps({
        "userId": int(userId),
        "acsessCode": "",
        "regionId": 1,
        "placeId": "0570",
        "clientId": "A63E01C2805",
        "dateTime": 1,
        "isContinue": 'false',
        "genericFlag": 0,
    })

    login_result = sdgb_api(data, "UserLoginApi", userId)
    return login_result

def logout(userId):
    data = json.dumps({
        "userId": int(userId),
        "accessCode":"",
        "regionId": 1,
        "placeId": "0570",
        "clientId": "A63E01C2805",
        "dateTime": 1,
        "type": 1
    })

    logout_result = sdgb_api(data, "UserLogoutApi", userId)
    return logout_result

def userdata(userId):
    data = json.dumps({
        "userId": int(userId)
    })

    userdata_result = sdgb_api(data, "GetUserDataApi", userId)

    return userdata_result

if __name__ == "__main__":
    userId = int(input())
    login(userId)
    print(userdata(userId))
    logout(userId)