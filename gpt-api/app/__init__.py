import logging

from sanic import Sanic
from .config import base
from .views import gpt
from .tasks import task_list


app = Sanic(__name__)

def create_app():
    app.blueprint(gpt, url_prefix="/api/v1/gpt")
    app.config.update(base)
    # register_tortoise(
    #     app, db_url=app.config["DB"], modules={"models": ["app.models"]}, generate_schemas=True
    # )

    for task in task_list:
        app.add_task(task)

    return app