from factory import create_app
from modules.tasks.app import celery

app = create_app()
app.app_context().push()
