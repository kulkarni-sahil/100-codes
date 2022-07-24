
from typing import Union


def is_positive(num: Union[int, float]):
    return "Positive" if num >= 0 else "Negative"

print(is_positive(num=15))