# -*- coding: utf-8 -*-

import sys

#Greeklish Converter

GREEKLISH_CHARS = ["a", "b", "g", "d", "e", "z", "i", "h", "k", "l", "m", "n", "x", "o", "w", "p", "r", "s", "t", "y", "f", "u", "v", "th", "ch", "ps", "ks"]
GREEKLISH_CHARS_CAPITALS = [char.upper() for char in GREEKLISH_CHARS]
GREEKLISH_CHARS_TITLES = [char.title() for char in GREEKLISH_CHARS]

GREEKLISH_TO_GREEK = {
    "a": "α",
    "b": "β",
    "g": "γ",
    "d": "δ",
    "e": "ε",
    "z": "ζ",
    "i": "ι",
    "h": "η",
    "k": "κ",
    "l": "λ",
    "m": "μ",
    "n": "ν",
    "x": "ξ",
    "o": "ο",
    "w": "ω",
    "p": "π",
    "r": "ρ",
    "s": "σ",
    "t": "τ",
    "y": "υ",
    "f": "φ",
    "u": "υ",
    "v": "β",
    "th": "θ",
    "ch": "χ",
    "ps": "ψ",
    "ks": "ξ",
}

GREEKLISH_TO_GREEK_CAPITALS = {k.upper():v.upper() for k,v in GREEKLISH_TO_GREEK.items()}
GREEKLISH_TO_GREEK_TITLES = {k.title():v.title() for k,v in GREEKLISH_TO_GREEK.items()}

#Check Input
if len(sys.argv) < 2:
    string = input("Type the sentence in greeklish:\n")
else:
    string = str(sys.argv[1])

converted_string = ""

### One pass for digrams
i = 0
while i < len(string):
    digram = string[i:i+2]
    if digram in GREEKLISH_CHARS:
        converted_string += GREEKLISH_TO_GREEK[digram]
        i += 1
    elif digram in GREEKLISH_CHARS_CAPITALS:
        converted_string += GREEKLISH_TO_GREEK_CAPITALS[digram]
        i += 1
    elif digram in GREEKLISH_CHARS_TITLES:
        converted_string += GREEKLISH_TO_GREEK_TITLES[digram]
        i += 1
    else:
        character = string[i]
        if character in GREEKLISH_CHARS_CAPITALS:
            converted_string += GREEKLISH_TO_GREEK_CAPITALS[character]
        elif character in GREEKLISH_CHARS:
            converted_string += GREEKLISH_TO_GREEK[character]
        elif character == '?':
            converted_string += ';'
        else:
            converted_string += character
    i += 1

#Convert σ to ς at the end of every word
converted_string_words = converted_string.split()
for i in range(0, len(converted_string_words)):
    if converted_string_words[i][-1] == 'σ':
        converted_string_words[i] = converted_string_words[i][:-1] + "ς"
converted_string = " ".join(converted_string_words)


print(converted_string)

# TODO
# 1. To for stin grammi 79 isws einai peritto, mporw na to sygxwneysw mesa sto while? (treat "s " as digram)
# 2. Mporw na kanw .isupper() anti na ftiaxnw olokliri lista me upper()?
# 3. Mporw na valw tous xamenous tonous me ti voitheia enos leksikou olwn twn ellinikwn leksewn.
