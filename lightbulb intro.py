from datetime import datetime
from typing import List


def sum_light(els: List[datetime]) -> int:
    """
    how long the light bulb has been turned on
    """
    return sum((e-b).total_seconds() for b, e in zip(els[0::2], els[1::2]))


if __name__ == "__main__":
    print("Example:")
    print(
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 13, 11, 0, 0),
            ]
        )
    )
