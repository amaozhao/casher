import base64
import json

from app01.wx import settings
from Crypto.Cipher import AES


class WXBizDataCrypt:
    def __init__(self, appId, sessionKey):
        self.appId = appId
        self.sessionKey = sessionKey

    def decrypt(self, encryptedData, iv):
        # base64 decode
        sessionKey = base64.b64decode(self.sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)

        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)

        decrypted = json.loads(self._unpad(cipher.decrypt(encryptedData)))

        if decrypted["watermark"]["appid"] != self.appId:
            raise Exception("Invalid Buffer")

        return decrypted

    def _unpad(self, s):
        return s[: -ord(s[len(s) - 1 :])]

    @classmethod
    def getInfo(cls, encryptedData, iv, session_key):
        return cls(settings.AppId, session_key).decrypt(encryptedData, iv)
