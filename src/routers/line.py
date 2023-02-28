from celery import group
from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.api import universities
from src.celery_tasks.tasks import sending_line_notify,sending_line_notify_n_times
from src.config.celery_utils import get_task_info
from src.schemas.schemas import Country

router = APIRouter(prefix='/line', tags=['Line'], responses={404: {"description": "Not found"}})

@router.post("/notify")
async def send_line_notify(notification_message: str, token: str):
    print(f"notification_message: {notification_message}")
    print(f"token: {token}")
    task = sending_line_notify.apply_async(args=[notification_message, token])
    return JSONResponse({"task_id": task.id})

@router.post("/notify_n")
async def send_line_notify_n_times(notification_message: str, token: str,n:int):
    print(f"notification_message: {notification_message}")
    print(f"token: {token}")
    task = sending_line_notify_n_times.apply_async(args=[notification_message, token,n])
    return JSONResponse({"task_id": task.id})
