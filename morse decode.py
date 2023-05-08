from timeit import timeit


MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code: str) -> str:
    # replace this for solution
    res = []
    for word in code.split('  '):
        for letter in word.split():
            res.append(MORSE[letter])
        res.append(' ')
    return ''.join(res).capitalize()[:-1]


def morse_decoder_opt(code):
    return ' '.join(''.join(map(MORSE.get, word.split()))
                    for word in code.split('   ')).capitalize()


print("Example:")
print(morse_decoder("... --- -- .   - . -..- -"))

itr = 1000000
code = "... --- -- .   - . -..- -"
for foo in [morse_decoder, morse_decoder_opt]:
    t = timeit(stmt="foo(code)", number=itr, globals=globals())
    print(f"{foo.__name__} run in {t:.6f} sec with {itr:,} iters.")
