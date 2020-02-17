from locust import HttpLocust, TaskSet, task, between
from tasks import show_quest_list
import settings

class HttpLocustUser(HttpLocust):
    host = settings.API_URL
    task_set = show_quest_list.ShowQuestListTask
    wait_time = between(2, 5)
    #min_wait = 2000
    #max_wait = 5000
