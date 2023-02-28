from typing import List

from celery import shared_task

from src.api import universities
import time


@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='universities:get_all_universities_task')
def get_all_universities_task(self, countries: List[str]):
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
