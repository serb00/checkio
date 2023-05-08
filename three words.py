def checkio(words: str) -> bool:
    # add your code here
    count = 0
    for word in words.split(' '):
        if not word[0].isnumeric():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False


print("Example:")
print(checkio("He is 123 man is 123 man"))

# These "asserts" are used for self-checking
# assert checkio("Hello World hello") == True
# assert checkio("He is 123 man") == False
# assert checkio("1 2 3 4") == False
