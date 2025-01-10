import json

from sdgb import sdgb_api
from settings import userId

def preview(userId):
    data = json.dumps({
        "userId": int(userId)
    })

    preview_result = sdgb_api(data, "GetUserPreviewApi", userId)

    return preview_result

if __name__ == "__main__":
    print(preview(userId))