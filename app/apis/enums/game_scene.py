# ゲームシーン
from enum import Enum

class GameScene(Enum):
    Dock = 0
    Quest = 1
    Battle = 2

    def __str__(self):
        return self.name