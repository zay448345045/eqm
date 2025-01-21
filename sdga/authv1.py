import base64
import urllib3
import zlib
import re

def DownloadOrder():
    ua = 'Windows/3.0'
    content = b'game_id=SDGA&ver=1.50&serial=A63E01E0048&encode=UTF-8'
    body = base64.b64encode(zlib.compress(content))
    http = urllib3.PoolManager()
    r = http.request(
        'POST',
        'http://naominet.jp/sys/servlet/DownloadOrder',
        body = body,
        headers = {
            'Pragma': 'DFI',
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
        }
    )
    resp_data = r.data
    response = zlib.decompress(base64.b64decode(resp_data)).decode()
    return response

def uri():
    data = DownloadOrder()
    pattern = r"https://[^\s]+"
    endpoint = re.search(pattern, data).group()
    http = urllib3.PoolManager()
    r = http.request(
        'GET',
        endpoint,
        headers = {
            'User-Agent': 'A63E01E0000',
        }
    )
    resp_data = r.data
    response = resp_data.decode()
    return response

if __name__ == "__main__":
    print(uri())
