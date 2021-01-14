from celery import Celery
from ext.db import db
from datetime import datetime
from ext.config import Config,config
from ext.celery import CELERY_TASK_LIST

celery = Celery( include=CELERY_TASK_LIST , broker=Config.CELERY_BROKER_URL)

#celery -A celery_worker.celery worker --loglevel=info --beat
#NORMAL RUN 
# celery -A celery_worker.celery worker --beat
#DEBUG CELERY 
# celery -A celery_worker.celery worker --loglevel=info --beat -l debug
@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    pass
    # Calls test('hello') every 10 seconds.
    # sender.add_periodic_task(1.0, test.s('hello'), name='add every 10')


@celery.task
def test(arg):
    print(datetime.now())
    print(arg)


# query = celery.events.state.tasks_by_type(your_task_name)
# # Kill tasks
# # Reference: http://docs.celeryproject.org/en/latest/userguide/workers.html#revoking-tasks
# for uuid, task in query:
#     celery.control.revoke(uuid, terminate=True)