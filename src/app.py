from flask import Flask

from client.habitica_client import Difficulty, TaskType, create_task
server = Flask(__name__)


@server.route("/create_task")
def handle_create_task():
    response = create_task(TaskType.TODO, "test", Difficulty.TRIVIAL)
    return response.text
