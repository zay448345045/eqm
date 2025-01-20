import json
import pytz

from sdgb import sdgb_api
from datetime import datetime

from settings import userId
from settings import regionId, clientId, placeId

def logout(timestamp):
    data = json.dumps({
        "userId": userId,
        "accessCode": "",
        "regionId": regionId,
        "placeId": placeId,
        "clientId": clientId,
        "dateTime": timestamp,
        "type": 1
    })

    logout_result = sdgb_api(data, "UserLogoutApi", userId)
    return logout_result
    

if __name__ == "__main__":
    print(logout(int(input())))
