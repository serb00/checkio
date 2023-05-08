from datetime import datetime


def backward_string_by_word(text: str) -> str:
    # your code here
    res = ''
    if len(text) > 0:
        for word in text.split(' '):
            for char in range(len(word), 0, -1):
                res += word[char-1]
            res += ' '
    return res[:-1]


def backward_string_by_word1(text: str) -> str:
    return ' '.join(word[::-1] for word in text.split(' '))


print("Example:")


iter = 1000000

start_time = datetime.now()


for i in range(iter):
    backward_string_by_word("... and so on ... alksjda;lskj asdlkja;sldkj as;"
                            "ldkja;sldkj;alkjs;alskj;lakjsd;lakjsd")

print(f'{iter} iterations with for loop took'
      f' { datetime.now() - start_time } seconds')

start_time = datetime.now()

for i in range(iter):
    backward_string_by_word1("... and so on ... alksjda;lskj asdlkja;sldkj as;"
                             "ldkja;sldkj;alkjs;alskj;lakjsd;lakjsd")

print(f'{iter} iterations with string functions took'
      f' { datetime.now() - start_time } seconds')
