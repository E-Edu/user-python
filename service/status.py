from enum import Enum


class Status(Enum):
    UNVERIFIED = 0
    VERIFIED = 1
    REPORTED = 2
    BANNED = 3
