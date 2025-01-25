import json
import zlib
import pytz
import hashlib
import httpx

from binascii import unhexlify, hexlify
import socket
import re

from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

AesKey = "A;mv5YUpHBK3YxTy5KB^[;5]C2AL50Bq"
AesIV = "9FM:sd9xA91X14v]"
ObfuscateParam = "M9aBNKuY"

class aes_pkcs7(object):
    def __init__(self, key: str, iv: str):
        self.key = key.encode('utf-8')
        self.iv = iv.encode('utf-8')
        self.mode = AES.MODE_CBC

    def encrypt(self, content: bytes) -> bytes:
        cipher = AES.new(self.key, self.mode, self.iv)
        content_padded = pad(content, AES.block_size)
        encrypted_bytes = cipher.encrypt(content_padded)
        return encrypted_bytes

    def decrypt(self, content):
        cipher = AES.new(self.key, self.mode, self.iv)
        decrypted_padded = cipher.decrypt(content)
        decrypted = unpad(decrypted_padded, AES.block_size)
        return decrypted

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
    return hashlib.md5((api+"MaimaiExp"+ObfuscateParam).encode()).hexdigest()

def sdgb_api(data, useApi, userId):
    aes = aes_pkcs7(AesKey,AesIV)
    data = bytes(data, encoding="utf-8")
    data_def = zlib.compress(data)
    data_enc = aes.encrypt(data_def)
    endpoint = "https://mai2exp.sic-rd1.jp:42081/Maimai2Servlet/"
    r = httpx.post(
        endpoint + get_hash_api(useApi),
        headers = {
            "User-Agent": "%s#%d"%(get_hash_api(useApi), userId),
            "Content-Type": "application/json",
            "Mai-Encoding": "1.51",
            "Accept-Encoding": "",
            "Charset": "UTF-8",
            "Content-Encoding": "deflate",
            "Expect": "100-continue"
        },
        data = data_enc
    )
    resp_enc = r.content
    try:
        resp_def = aes.decrypt(resp_enc)
    except:
        resp_def = resp_enc
    return zlib.decompress(resp_def).decode('utf-8')

def felica(IDm):
    key = b'Copyright(C)SEGA'
    # https://sega.bsnk.me/allnet/aimedb/common/
    magic = "3ea1"
    version = "2140"
    command_id = "0100" # ID = 1
    length = "3000" # 48
    gameId = "534447410000" # SDGA
    storeId = "aa1e0000"
    keychip_ID = "413633453031453031383200" # A63E01E0264
    header = magic + version + command_id + length + "0000" + gameId + storeId + keychip_ID

    IDm = str(IDm)
    PMm = "00F1000000014300"

    plaintext_hex_stream = header + IDm + PMm

    plaintext = unhexlify(plaintext_hex_stream)

    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_message = cipher.encrypt(plaintext)

    encrypted_hex_stream = hexlify(encrypted_message).decode('utf-8')

    server_address = ('aime.naominet.jp', 22345)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(server_address)
        sock.sendall(encrypted_message)

        response = sock.recv(1024)

        decrypted_response = cipher.decrypt(response)

        decrypted_hex_stream = hexlify(decrypted_response).decode('utf-8')

    return decrypted_hex_stream[-24:-4]

def aimedb_api(accessCode):
    key = b'Copyright(C)SEGA'
    # https://sega.bsnk.me/allnet/aimedb/common/
    magic = "3ea1"
    version = "2140"
    command_id = "0f00" # ID = 15
    length = "3000" # 48
    gameId = "534447410000" # SDGA
    storeId = "aa1e0000"
    keychip_ID = "413633453031453031383200" # A63E01E0264
    header = magic + version + command_id + length + "0000" + gameId + storeId + keychip_ID

    access_code = str(accessCode)
    end_stream = "000201020304"


    plaintext_hex_stream = header + access_code + end_stream

    plaintext = unhexlify(plaintext_hex_stream)

    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_message = cipher.encrypt(plaintext)

    encrypted_hex_stream = hexlify(encrypted_message).decode('utf-8')

    server_address = ('aime.naominet.jp', 22345)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(server_address)
        sock.sendall(encrypted_message)

        response = sock.recv(1024)

        decrypted_response = cipher.decrypt(response)

        decrypted_hex_stream = hexlify(decrypted_response).decode('utf-8')

        match = re.search(r'[0-9a-f]{64}([0-9a-f]{6})', decrypted_hex_stream)
        if match:
            six_digit_code = match.group(1)

            rearranged_hex = six_digit_code[4:6] + six_digit_code[2:4] + six_digit_code[0:2]
    
            decimal_value = int(rearranged_hex, 16)
            return decimal_value
