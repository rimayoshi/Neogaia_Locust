import msgpack
from locust import HttpLocust, TaskSet, task

class MyApiStressTask(TaskSet):
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
        print('task start')
        ret = self.client.get("/api/masterdata/get")
        print('task finish')

class MyApiStressMain(HttpLocust):
    host = 'http://localhost:8080' ## 負荷テスト対象のホスト指定
    task_set = TestTask
    min_wait = 2000
    max_wait = 5000

###
# 1. コマンドラインでlocustサーバ起動
# locust -f samples/sample_apistress.py
# 2. ブラウザで http://localhost:8089 にアクセスするとlocust管理ページにいける
###