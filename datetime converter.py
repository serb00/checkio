from datetime import datetime


def date_time(time: str) -> str:
    # %-d for linux
    # %#d for windows
    dt = datetime.strptime(time, '%d.%m.%Y %H:%M')
    return dt.strftime(f'%#d %B %Y year %#H hour'
                       f'{"" if dt.hour == 1 else "s"} %#M minute'
                       f'{"" if dt.minute == 1 else "s"}')


print("Example:")
print(date_time("09.07.1995 01:01"))
