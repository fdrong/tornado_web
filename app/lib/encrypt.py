# coding:utf-8
import base64
import hashlib
import random
from Crypto import Random
from Crypto.Cipher import AES
import uuid


# 产生全局唯一表示符
def get_a_uuid():
    # r_uuid = base64.urlsafe_b64encode(uuid.uuid1().bytes)
    return uuid.uuid1().hex


# 生成一个随机密码
def random_passwd(randomlength=10):
    passwd = ''
    chars = '!@#$%&*/AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    strings = random.Random()
    for i in range(randomlength):
        passwd += chars[strings.randint(0, length)]
    return passwd


# md5加密
def md5_encrypt(pwd):
    md5 = hashlib.md5()
    md5.update(pwd)
    return md5.hexdigest()


# 两次md5加密
def md5_twice(pwd):
    md5_pwd = md5_encrypt(pwd)
    return md5_encrypt(md5_pwd)


# 返回文件的16进制字符串
def hex_file(filepath):
    content = []
    with open(filepath, "rb") as f:
        for line in f:
            hexdata = line.encode("hex")
            content.append(hexdata)
    return "".join(content)


# AES加密解密类
class AESCipher(object):
    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]