from enum import Enum


class Role(Enum):
    USER = 0
    TEACHER = 1
    ADMIN = 2
    PRIVILEGED_STUDENT = 3
