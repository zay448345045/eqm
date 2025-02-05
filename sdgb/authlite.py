import dataclasses
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import httpx

def enc(key, iv, data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(data)
    return encrypted

def dec(key, iv ,data):
    de_cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = de_cipher.decrypt(data)
    return decrypted

def hello():
    key = bytes([ 47, 63, 106, 111, 43, 34, 76, 38, 92, 67, 114, 57, 40, 61, 107, 71 ])
    #key = bytes([ 45, 97, 53, 55, 85, 88, 52, 121, 57, 47, 104, 40, 73, 109, 65, 81 ])
    iv = bytes.fromhex('00000000000000000000000000000000')
    ua = 'SDGB;Windows/Lite'  
    #ua = 'SDHJ;Windows/Lite'
    content = bytes([0] * 16) + b'title_id=SDGB&title_ver=1.41&client_id=A63E01C2805&token=205648745'
    #content = bytes([0] * 16) + b'title_id=SDHJ&title_ver=1.11&client_id=A63E01E1326&token=205648745'
    header = bytes.fromhex('00000000000000000000000000000000')
    bytes_data = pad(header + content, 16) 
    encrypted = enc(key, iv, bytes_data)
    r = httpx.post(
        'http://at.sys-allnet.cn/net/delivery/instruction',
        data = encrypted,
        headers = {
            'User-Agent': ua,
            'Pragma': 'DFI'
        }
    )
    resp_data = r.content
    decrypted = dec(key, resp_data[:16], resp_data)
    decrypted_bytes = decrypted[16:]
    decrypted_str = decrypted_bytes.decode('UTF-8')
    print(decrypted_str)

hello()