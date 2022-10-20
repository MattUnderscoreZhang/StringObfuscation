import json
import random


empty_unicode_chars = [
    '\u200b', '\u200c', '\u200d', '\u2060', '\u2061', '\u2062', '\u2063',
    '\u2064', '\u2065', '\u2066', '\u2067', '\u2068', '\u2069', '\u206a',
    '\u206b', '\u206c', '\u206d', '\u206e', '\u206f', '\ufeff', '\u00ad',
    '\u034f', '\u061c', '\u115f', '\u1160', '\u17b4', '\u17b5', '\u180e',
    '\u200b', '\u200c', '\u200d', '\u200e', '\u200f', '\u2060', '\u2061',
    '\u2062', '\u2063', '\u2064', '\u206a', '\u206b', '\u206c', '\u206d',
    '\u206e', '\u206f', '\u3164', '\ufeff', '\uffa0',
]

lookalike_unicode_chars = {
    "i": [ '\u0456', ],
    "o": [ '\u1d0f', "\u043e", "\u03bf", "\u0585", ],
    "a": [ '\u0430', ],
    "e": [ '\u0435', ],
    "u": [ '\u057d', ],
    "c": [ "\u0441", ],
    # "d": [ "\u0501", ],
    "h": [ "\u04bb" ],
    "j": [ '\u0458', ],
    "l": [ "\u04cf", ],
    "n": [ "\u0578" ],
    "p": [ "\u0440" ],
    "x": [ "\u0445", ],
    "y": [ "\u0443", ],
    ".": [ '\u2024', ],
}

def obfuscate_string(string: str) -> str:
    # retain extension if present
    if (len(string) > 4 and string[-3] == '.') or (len(string) > 5 and string[-4] == '.'):
        string, extension = string.rsplit('.', 1)
    else:
        string, extension = string, None
    # add random empty unicode chars
    random_bools = [random.choice([True, False]) for _ in range(len(string))]
    if sum(random_bools) == 0:
        random_bools[0] = True
    for i in range(len(string)):
        if random_bools[i]:
            string = string[:i] + random.choice(empty_unicode_chars) + string[i:]
    # replace random letters with lookalikes
    replace_chance = 0.2
    for i in range(len(string)):
        if string[i] in lookalike_unicode_chars and random.random() < replace_chance:
            # replace char i in string
            string = string[:i] + random.choice(lookalike_unicode_chars[string[i]]) + string[i+1:]
    # replace extension
    if extension is not None:
        return string + '.' + extension
    return string

for _ in range(10):
    # string = 'explorer.exe'
    string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    print(obfuscate_string(string))
