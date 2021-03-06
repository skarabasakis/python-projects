# -*- coding: utf-8 -*-

import sys

#Greeklish Converter

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
    "t": "τ",
    "y": "υ",
    "f": "φ",
    "u": "υ",
    "v": "β",
    "th": "θ",
    "ch": "χ",
    "ps": "ψ",
    "ks": "ξ"
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
    if digram in GREEKLISH_TO_GREEK:
        converted_string += GREEKLISH_TO_GREEK[digram]
        i += 1
    elif digram in GREEKLISH_TO_GREEK_CAPITALS:
        converted_string += GREEKLISH_TO_GREEK_CAPITALS[digram.upper()]        
        i += 1
    elif digram in GREEKLISH_TO_GREEK_TITLES:
        converted_string += GREEKLISH_TO_GREEK_TITLES[digram.title()]
        i += 1

    elif digram[0].lower() == 's':
        if len(digram) == 2 and digram[1].isalpha():
            converted_string += "Σ" if digram[0].isupper() else 'σ'
        else:
            converted_string += "Σ" if digram[0].isupper() else 'ς'

    else:
        character = string[i]
        if character.isupper():
            converted_string += GREEKLISH_TO_GREEK_CAPITALS[character]
        elif character in GREEKLISH_TO_GREEK:
            converted_string += GREEKLISH_TO_GREEK[character]
        elif character == '?':
            converted_string += ';'
        else:
            converted_string += character

    i += 1


print(converted_string)

# TODO
# 1. To for stin grammi 79 isws einai peritto, mporw na to sygxwneysw mesa sto while? (treat "s " as digram) -> PENDING
# 2. Mporw na kanw .isupper() anti na ftiaxnw olokliri lista me upper()? -> DONE
# 3. Mporw na valw tous xamenous tonous me ti voitheia enos leksikou olwn twn ellinikwn leksewn. -> PENDING
