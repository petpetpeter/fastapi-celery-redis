import requests
import json
import logging
import time


url = 'https://notify-api.line.me/api/notify'

def send_line_notify(notification_message,token):
    headers = {'Authorization':'Bearer '+token}
    payload = {'message': notification_message}
    line_notify = requests.post(url, headers = headers, data = payload)
    return line_notify.status_code

