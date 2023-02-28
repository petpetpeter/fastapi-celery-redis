from typing import List

from celery import shared_task

from src.api import universities
from src.api import line_notify
import time


@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='universities:get_all_universities_task')
def get_all_universities_task(self, countries: List[str]):
    print(f"start get_all_universities_task: {countries}")
    data: dict = {}
    for i,cnt in enumerate(countries):
        self.update_state(state='PROGRESS', meta={'percent': i/len(countries)*100,"country":cnt})
        data.update(universities.get_all_universities_for_country(cnt))
        time.sleep(5)
    return data


@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='university:get_university_task')
def get_university_task(self, country: str):
    university = universities.get_all_universities_for_country(country)
    return university

@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='line:sending_line_notify')
def sending_line_notify(self, notification_message,token):
    line_notify.send_line_notify(notification_message,token)
    return "success"

@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
                name='line:sending_line_notify_n_times')
def sending_line_notify_n_times(self, notification_message,token,n):
    for i in range(n):
        self.update_state(state='PROGRESS', meta={'percent': i/n*100})
        message = notification_message + "_" + str(i)
        line_notify.send_line_notify(message,token)
    return "success"
