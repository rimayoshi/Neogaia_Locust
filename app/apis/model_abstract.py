from abc import ABCMeta
from datetime import datetime
from enum import Enum
import msgpack

def unpack_datetime(code, data):
    """
    msgpack.unpackb() によるデータ復元時にDateTime型を復元するための拡張関数
    """
    if code == -1:
        if len(data) == 4:
            secs = int.from_bytes(data, byteorder='big', signed=True)
            nsecs = 0;
        elif len(data) == 8:
            data = int.from_bytes(data, byteorder='big', signed=False)
            secs = data & 0x00000003ffffffff;
            nsecs = data >> 34;
        elif len(data) == 12:
            import struct
            nsecs, secs = struct.unpack('!Iq', data)
        else:
            raise AssertionError("Not reached");
        return datetime.utcfromtimestamp(secs + nsecs / 1e9)
    else:
        return msgpack.ExtType(code, data)

def pack(data):
    return msgpack.packb(data)

def unpack(data):
    return msgpack.unpackb(data, ext_hook=unpack_datetime, encoding='utf-8')

def toPascalCase(text):
    if len(text) > 1:
        return text[0].upper() + text[1:]
    elif len(text) == 1:
        return text[0].upper()
    else:
        return text

class ModelAbstract(metaclass=ABCMeta):
    def __init__(self, data:dict):
        if data is None:
            return
        for key in data:
            value = data[key]
            if value is None:
                continue
            elif key in self.KEYS.values():
                setter = 'set' + toPascalCase(key)
            elif isinstance(key, int) and key in self.KEYS:
                setter = 'set' + toPascalCase(self.KEYS[key])
            else:
                continue
            invoker = getattr(self, setter)
            invoker(value)

    def __convertValue(self, value):
        if isinstance(value, list):
            ret = []
            for elem in value:
                ret.append(self.__convertValue(elem))
            return ret
        elif isinstance(value, datetime):
            return value.timestamp()
        elif isinstance(value, Enum):
            return value.value
        elif isinstance(value, ModelAbstract):
            return value.toIntKeyDict()
        else:
            return value

    def toIntKeyDict(self):
        ret = {}
        for index in self.KEYS:
            value = getattr(self, self.KEYS[index])
            if value is None:
                continue
            ret[index] = self.__convertValue(value)
        return ret

    @classmethod
    def toDictFromIntKeyDict(self, data):
        ret = {}
        for index in data:
            keyName = self.KEYS.get(index)
            if keyName is None:
                continue
            ret[keyName] = data[index]
        return ret

    def pack(self):
        return pack(self.toIntKeyDict())

    @classmethod
    def unpack(self, data):
        return self.toDictFromIntKeyDict(unpack(data))

class RequestModelAbstract(ModelAbstract, metaclass=ABCMeta):
    def __init__(self, data=None):
        self.__seq = 0
        super().__init__(data)

    def getApiPath(self):
        return self.API_PATH

    def getPackedParams(self):
        result = {'req': self.pack(), 'seq': self.__seq}
        self.__seq += 1
        return result
