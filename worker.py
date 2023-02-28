from main import celery

argv = [
    'worker',
    '--loglevel=info',
    '-c 1',
    '-S redbeat.RedBeatScheduler',
    '--beat',
]

if __name__ == '__main__':
    celery.worker_main(argv)