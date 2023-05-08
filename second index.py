from datetime import datetime


def second_index(text: str, symbol: str) -> [int, None]:
    """
    returns the second index of a symbol in a given text
    """
    # your code here
    ind = 0
    skiped = False
    for char in text:
        if char == symbol and not skiped:
            skiped = True
        elif char == symbol and skiped:
            return ind
        ind += 1
    return None

def second_index_opt(text: str, symbol: str) -> [int, None]:
    second = text.find(symbol, text.find(symbol) + 1)
    return second if second != -1 else None


print("Example:")


iter = 10000000

start_time = datetime.now()


for i in range(iter):
    second_index("sims", "s")

print(f'{iter} iterations with for loop took'
      f' { datetime.now() - start_time } seconds')


start_time = datetime.now()


for i in range(iter):
    second_index_opt("sims", "s")

print(f'{iter} iterations with find function took'
      f' { datetime.now() - start_time } seconds')
