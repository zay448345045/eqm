import json
import pytz

from sdgb import sdgb_api
from datetime import datetime

from settings import userId
from settings import regionId, clientId, placeId

def login(timestamp):
    data = json.dumps({
        "userId": userId,
        "accessCode": "",
        "regionId": regionId,
        "placeId": placeId,
        "clientId": clientId,
        "dateTime": timestamp,
        "isContinue": False,
        "genericFlag": 0,
    })

    login_result = sdgb_api(data, "UserLoginApi", userId)
    return login_result

if __name__ == "__main__":
    print(login(int(input())))
