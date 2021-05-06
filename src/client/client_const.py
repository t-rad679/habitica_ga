# HTTP Methods
from enum import Enum


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

    TODO = "TODO"
    DAILY = "DAILY"
    HABIT = "HABIT"