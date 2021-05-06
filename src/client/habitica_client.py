import requests
import json
from enum import Enum

CREATE_TASK_ENDPOINT = "/api/v3/tasks/user"

DOMAIN = 'https://www.habitica.com'

HEADERS = {
    "Content-type": "application/json",
    "x-client": "38dab3a1-320a-47ee-a246-8923d652d985-googleassistant",
    "x-api-user": "38dab3a1-320a-47ee-a246-8923d652d985",
    "x-api-key": "62cf292a-0390-46ff-a91c-e763cd81be9a"
}


def create_task(task_type, task_text, difficulty):
    """
    Calls the Habitica API to create a task

    Arguments:
        task_type: client_const.TaskType The type of task
        task_text: string The text that will be displayed for the task in the main task view
        difficulty: client_const.Difficulty The difficulty (or priority, to the habitica API) of the task
    Returns:
        response: the response for the create task call
    """

    body = json.dumps({
        "type": task_type.value,
        "text": task_text,
        "priority": difficulty.value,
    })
    response = requests.post("{}{}".format(DOMAIN, CREATE_TASK_ENDPOINT), headers=HEADERS, data=body)
    return response


class HttpMethod(Enum):
    """
    Standard HTTP methods
    """

    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    DELETE = "DELETE"


class Difficulty(Enum):
    """
    Difficulty setting for the task. Known by the Habitica API as priority
    """

    TRIVIAL = 0.1
    EASY = 1
    MEDIUM = 1.5
    HARD = 2


class TaskType(Enum):
    """
    The type of task
    """

    TODO = "todo"
    DAILY = "daily"
    HABIT = "habit"
    REWARD = "reward"
