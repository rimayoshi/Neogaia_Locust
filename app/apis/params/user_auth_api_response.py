# ユーザ認証レスポンスパラメータ
from apis.model_abstract import ModelAbstract
from apis.structs.user import User

class UserAuthApiResponse(ModelAbstract):
    KEYS = {
        1: 'user',
    }

    def __init__(self, data=None):
        self.user = None
        super().__init__(data)

    def getUser(self):
        return self.user

    def setUser(self, data):
        if data is None or isinstance(data, User):
            self.user = data
        else:
            self.user = User(data)

    def __str__(self):
        L = []
        L.append('{')
        L.append(f"user: {self.getUser()}")
        L.append('}')
        return ''.join(L)