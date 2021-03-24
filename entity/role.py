from enum import Enum

class Role(Enum):
    Reader = "Reader"
    Writer = "Writer"

# Reader - These users can view to-dos but not change or create new ones
# Writer - These users can also change existing to-dos or create new ones