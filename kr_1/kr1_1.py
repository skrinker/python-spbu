from datetime import datetime
from functools import update_wrapper
from typing import Callable, List, Any, Tuple
from typing import Optional, Callable, Any


class Spy:
    def __init__(self, function: Callable):
        self._function = function
        self.logs: List[Tuple] = []
        update_wrapper(self, function)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        current = datetime.now()
        params = {"args": args, "kwargs": kwargs}
        self.logs.append((current, params))

        return self._function(*args, **kwargs)


def print_usage_statistic(function: Callable):
    if isinstance(function, Spy):
        for log in function.logs:
            yield log
        return

    raise TypeError("The function should be decorated with @Spy.")

