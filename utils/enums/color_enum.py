from enum import Enum 

class Status(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

    def __str__(self):
        return self.name