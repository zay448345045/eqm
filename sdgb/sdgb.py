import json
import zlib
import pytz
import base64
import hashlib
import httpx

from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

AesKey = "n7bx6:@Fg_:2;5E89Phy7AyIcpxEQ:R@"
AesIV = ";;KjR1C3hgB1ovXa"
ObfuscateParam = "BEs2D5vW"
KeychipID = "A63E-01C28055905"

class aes_pkcs7(object):
    def __init__(self, key: str, iv: str):
        self.key = key.encode('utf-8')
        self.iv = iv.encode('utf-8')
        self.mode = AES.MODE_CBC

    def encrypt(self, content):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        content_padding = self.pkcs7padding(content)
        encrypt_bytes = cipher.encrypt(content_padding.encode('utf-8'))
        return encrypt_bytes
        return base64.b64encode(encrypt_bytes)

    def decrypt(self, content):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return cipher.decrypt(content)
        text = cipher.decrypt(content).decode('utf-8')
        return self.pkcs7unpadding(text)

    def pkcs7unpadding(self, text):
        length = len(text)
        unpadding = ord(text[length - 1])
        return text[0:length - unpadding]

    def pkcs7padding(self, text):
        bs = 16
        length = len(text)
        bytes_length = len(text.encode('utf-8'))
        padding_size = length if (bytes_length == length) else bytes_length
        padding = bs - padding_size % bs
        padding_text = chr(padding) * padding
        return text + padding_text

def get_hash_api(api):
    return hashlib.md5((api+"MaimaiChn"+ObfuscateParam).encode()).hexdigest()

def sdgb_api(data, useApi, userId):
    aes = aes_pkcs7(AesKey,AesIV)
    data = data
    data_enc = aes.encrypt(data)
    data_def = zlib.compress(data_enc)
    endpoint = "https://maimai-gm.wahlap.com:42081/Maimai2Servlet/"
    r = httpx.post(
        endpoint + get_hash_api(useApi),
        headers = {
            "User-Agent": "%s#%d"%(get_hash_api(useApi), userId), 
            "Content-Type": "application/json",
            "Mai-Encoding": "1.40",
            "Accept-Encoding": "",
            "Charset": "UTF-8", 
            "Content-Encoding": "deflate", 
            "Expect": "100-continue"
        },
        data = data_def
    )
    resp_def = r.content

    try:
        resp_enc = zlib.decompress(resp_def)
    except:
        resp_enc = resp_def
    return unpad(aes.decrypt(resp_enc), 16).decode()

def qr_api(qr_code):
    if len(qr_code) > 64:
        qr_code = qr_code[-64:]
    time_stamp = datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%y%m%d%H%M%S")
    auth_key = hashlib.sha256(
        (KeychipID + time_stamp + "XcW5FW4cPArBXEk4vzKz3CIrMuA5EVVW").encode("UTF-8")).hexdigest().upper()
    param = {
        "chipID": KeychipID,
        "openGameID": "MAID",
        "key": auth_key,
        "qrCode": qr_code,
        "timestamp": time_stamp
    }
    headers = {
        "Contention": "Keep-Alive",
        "Host": "ai.sys-all.cn",
        "User-Agent": "WC_AIME_LIB"
    }
    res = httpx.post(
        "http://ai.sys-allnet.cn/wc_aime/api/get_data",
        data = json.dumps(param, separators=(',', ':')),
        headers = headers
    )
    assert res.status_code == 200, "网络错误"
    return json.loads(res.content)