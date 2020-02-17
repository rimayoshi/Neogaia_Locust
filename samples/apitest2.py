from datetime import datetime
import json
from locust import HttpLocust, TaskSet, task
import msgpack

def ext_hook(code, data):
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

class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    def login(self):
        print('login')
    
    def logout(self):
        print('logout')

    @task
    def my_task(self):
        print('start')
        requestParams = {1: 1001, 2: 1, 3: 1}; ## 1=npsn, 2=token, 3=npaCode
        packedParams = msgpack.packb(requestParams)
        ret = self.client.post("/api/user/auth", {'req': packedParams})
        print('レスポンス:', ret.content)
        ret2 = msgpack.unpackb(ret.content, ext_hook=ext_hook, encoding='utf-8')
        print('解凍後:', ret2)
        ret3 = msgpack.unpackb(ret2[2], ext_hook=ext_hook, encoding='utf-8')
        print('解凍後のdataを更に解凍:', ret3)

class RedmineUser(HttpLocust):
    #host = settings.API_URL
    host = 'http://localhost:8080'
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 5000