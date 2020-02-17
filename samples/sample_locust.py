from locust import Locust, TaskSet, task

class MyLocustTask(TaskSet):
    @task
    def my_task(self):
        print("Locust instance (%r) executing my_task" % (self.locust))

class MyLocustMain(Locust):
    task_set = MyLocustTask
    min_wait = 1000
    max_wait = 2000

###
# 1. コマンドラインでlocustサーバ起動
# locust -f samples/sample_locust.py
# 2. ブラウザで http://localhost:8089 にアクセスするとlocust管理ページにいける
###
