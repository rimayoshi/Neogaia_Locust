# ユーザ認証リクエストパラメータ
from apis.model_abstract import RequestModelAbstract

class UserAuthApiRequest(RequestModelAbstract):
    API_PATH = '/api/user/auth'
    KEYS = {
        1: 'npsn',
        2: 'token',
        3: 'npaCode',
    }

    def __init__(self, data=None):
        self.npsn = None
        self.token = None
        self.npaCode = None
        super().__init__(data)

    def getNpsn(self):
        return self.npsn

    def setNpsn(self, data):
        self.npsn = data

    def getToken(self):
        return self.token

    def setToken(self, data):
        self.token = data

    def getNpaCode(self):
        return self.npaCode

    def setNpaCode(self, data):
        self.npaCode = data

    def __str__(self):
        L = []
        L.append('{')
        L.append(f"npsn: '{self.getNpsn()}', ")
        L.append(f"token: '{self.getToken()}', ")
        L.append(f"npaCode: {self.getNpaCode()}")
        L.append('}')
        return ''.join(L)