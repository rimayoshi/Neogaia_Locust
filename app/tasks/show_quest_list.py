from locust import TaskSet, task
from tasks.common.login_task_set import *

class ShowQuestListTask(LoginTaskSet):
    def on_start(self):
        self.login('1001', '1', '1')

    @task
    def my_task(self):
        print(self.user)
        return
