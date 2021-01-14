from modules.tasks.app import celery

@celery.task
def test2(arg):
    print(arg)