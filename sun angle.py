from timeit import timeit
from typing import Union


def sun_angle(time: str) -> Union[float, str]:
    # replace this for solution
    angle_per_minute = 180 / (60 * 12)
    res = time.split(':')
    minutes = (int(res[0])-6) * 60 + int(res[1])
    return (angle_per_minute * minutes if 0 <= minutes <= 720
            else "I don't see the sun!")


def sun_angle_opt(time):
    hh, mm = map(int, time.split(':'))
    tt = hh*60+mm

    return "I don't see the sun!" if (tt < 360 or 1080 < tt) else (tt-360)*0.25


print("Example:")
print(sun_angle("15:47"))
print(sun_angle_opt("08:12"))

time = "08:12"
for foo in [sun_angle, sun_angle_opt]:
    t = timeit(stmt="foo(time)", number=100000, globals=globals())
    print(f"{foo.__name__} took: {t:.5f}")
