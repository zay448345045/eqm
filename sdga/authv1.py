import base64
import zlib
import re
import httpx

def DownloadOrder():
    ua = 'Windows/3.0'
    content = b'game_id=SDGA&ver=1.50&serial=A63E01E0048&encode=UTF-8'
    body = base64.b64encode(zlib.compress(content))
    r = httpx.post(
        'http://naominet.jp/sys/servlet/DownloadOrder',
        data = body,
        headers = {
            'Pragma': 'DFI',
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
        }
    )
    resp_data = r.content
    response = zlib.decompress(base64.b64decode(resp_data)).decode()
    return response

def uri():
    data = DownloadOrder()
    pattern = r"https://[^\s]+"
    endpoint = re.search(pattern, data).group()
    r = httpx.get(
        endpoint,
        headers = {
            'User-Agent': 'A63E01E0000',
        }
    )
    resp_data = r.content
    response = resp_data.decode()
    return response

if __name__ == "__main__":
    print(uri())
