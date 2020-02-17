# ユーザ認証レスポンスパラメータ
from apis.model_abstract import ModelAbstract
from apis.enums.game_scene import GameScene
from datetime import datetime

class User(ModelAbstract):
    KEYS = {
        1: 'userId',
        2: 'npsn',
        3: 'npToken',
        4: 'playerId',
        5: 'name',
        6: 'comment',
        7: 'rank',
        8: 'exp',
        9: 'armsStorageLimit',
        10: 'autoExtraction',
        11: 'supportSeekerId',
        12: 'lastScene',
        13: 'lastSessionId',
        14: 'lastLoginAt',
    }

    def __init__(self, data=None):
        self.userId = None
        self.npsn = None
        self.npToken = None
        self.playerId = None
        self.name = None
        self.comment = None
        self.rank = None
        self.exp = None
        self.armsStorageLimit = None
        self.autoExtraction = None
        self.supportSeekerId = None
        self.lastScene = None
        self.lastSessionId = None
        self.lastLoginAt = None
        super().__init__(data)

    def getUserId(self):
        return self.userId

    def setUserId(self, data: int):
        self.userId = data

    def getNpsn(self):
        return self.npsn

    def setNpsn(self, data: str):
        self.npsn = data

    def getNpToken(self) -> str:
        return self.npToken

    def setNpToken(self, data: str):
        self.npToken = data

    def getPlayerId(self) -> str:
        return self.playerId

    def setPlayerId(self, data: str):
        self.playerId = data

    def getName(self) -> str:
        return self.name

    def setName(self, data: str):
        self.name = data

    def getComment(self) -> str:
        return self.comment

    def setComment(self, data: str):
        self.comment = data

    def getRank(self) -> int:
        return self.rank

    def setRank(self, data: int):
        self.rank = data

    def getExp(self) -> int:
        return self.exp

    def setExp(self, data: int):
        self.exp = data

    def getArmsStorageLimit(self) -> int:
        return self.armsStorageLimit

    def setArmsStorageLimit(self, data: int):
        self.armsStorageLimit = data

    def getAutoExtraction(self) -> bool:
        return self.autoExtraction

    def setAutoExtraction(self, data: bool):
        self.autoExtraction = data

    def getSupportSeekerId(self) -> int:
        return self.supportSeekerId

    def setSupportSeekerId(self, data: int):
        self.supportSeekerId = data

    def getLastScene(self) -> GameScene:
        return self.lastScene

    def setLastScene(self, data):
        if data is None or isinstance(data, GameScene):
            self.lastScene = data
        else:
            self.lastScene = GameScene(data)

    def getLastSessionId(self) -> str:
        return self.lastSessionId

    def setLastSessionId(self, data: str):
        self.lastSessionId = str(data)

    def getLastLoginAt(self) -> datetime:
        return self.lastLoginAt

    def setLastLoginAt(self, data):
        if data is None or isinstance(data, datetime):
            self.lastLoginAt = data
        else:
            self.lastLoginAt = datetime.fromtimestamp(data)

    def __str__(self):
        L = []
        L.append('{')
        L.append(f"userId: {self.getUserId()}, ")
        L.append(f"npsn: '{self.getNpsn()}', ")
        L.append(f"npToken: '{self.getNpToken()}', ")
        L.append(f"playerId: '{self.getPlayerId()}', ")
        L.append(f"name: '{self.getName()}', ")
        L.append(f"comment: '{self.getComment()}', ")
        L.append(f"rank: {self.getRank()}, ")
        L.append(f"exp: {self.getExp()}, ")
        L.append(f"armsStorageLimit: {self.getArmsStorageLimit()}, ")
        L.append(f"autoExtraction: {self.getAutoExtraction()}, ")
        L.append(f"supportSeekerId: {self.getSupportSeekerId()}, ")
        L.append(f"lastScene: {self.getLastScene()}, ")
        L.append(f"lastSessionId: {self.getLastSessionId()}, ")
        L.append(f"lastLoginAt: '{self.getLastLoginAt()}'")
        L.append('}')
        return ''.join(L)