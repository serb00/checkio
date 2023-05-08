from datetime import datetime


def between_markers(text: str, begin: str, end: str) -> str:
    """
    returns substring between two given markers
    """
    # your code here
    return text[text.find(begin)+len(begin) if begin in text else None:
                text.find(end) if end in text else None]


def between_markers1(text: str, begin: str, end: str) -> str:
    return text[text.index(begin)+len(begin) if begin in text else None:
                text.index(end) if end in text else None]


print("Example:")

iter = 10000000

start_time = datetime.now()


for i in range(iter):
    between_markers("Never send a human to do a machine's job.",
                    'Never', 'do')

print(f'{iter} iterations with string.find() took'
      f' { datetime.now() - start_time } seconds')

start_time = datetime.now()

for i in range(iter):
    between_markers1("Never send a human to do a machine's job.",
                     'Never', 'do')

print(f'{iter} iterations with string in string functions took'
      f' { datetime.now() - start_time } seconds')
