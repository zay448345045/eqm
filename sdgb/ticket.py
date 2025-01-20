import json
import pytz
import time

from sdgb import sdgb_api
from datetime import datetime, timedelta

from settings import userId
from settings import regionId, clientId, placeId

from logout import logout
from login import login

def get_ticket():
    data = json.dumps({
        "userId": userId,
        "userCharge": {
            "chargeId": 6,
            "stock": 1,
            "purchaseDate": (datetime.now(pytz.timezone('Asia/Shanghai')) - timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S.0"),
            "validDate": (datetime.now(pytz.timezone('Asia/Shanghai')) - timedelta(hours=1) + timedelta(days=90)).replace(hour=4, minute=0, second=0).strftime("%Y-%m-%d %H:%M:%S")
        },
        "userChargelog": {
            "chargeId": 6,
            "price": 4,
            "purchaseDate": (datetime.now(pytz.timezone('Asia/Shanghai')) - timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S.0"),
            "placeId": placeId,
            "regionId": regionId,
            "clientId": clientId
        }
    })

    ticket_result = sdgb_api(data, "UpsertUserChargelogApi", userId)

    return ticket_result

if __name__ == "__main__":
    timestamp = int(time.time())
    print(timestamp)
    print(login(timestamp))
    print(get_ticket())
    print(logout(timestamp))
