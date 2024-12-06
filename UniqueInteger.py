import random
from typing import Self


class UniqueInteger:
    def __init__(self, max_digits: int) -> None:
        self._max_number: int = 10**max_digits - 1
        self._chosen: set[int] = set()

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        if len(self._chosen) == self._max_number + 1:
            raise OverflowError("no more unique integers available")
        while True:
            integer = random.randint(0, self._max_number)
            if integer in self._chosen:
                continue
            else:
                self._chosen.add(integer)
                return integer
