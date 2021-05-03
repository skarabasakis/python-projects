# -*- coding: utf-8 -*-

import sys

#Greeklish Converter

GREEKLISH_CHARS = ["a", "b", "g", "d", "e", "ai", "z", "i", "h", "ei", "oi", "th", "k", "l", "m", "n", "x", "o", "w", "p", "r", "s", "t", "y", "f", "ch", "ps", " ", ","]
GREEKLISH_CHARS_CAPITALS = [char.upper() for char in GREEKLISH_CHARS]

GREEKLISH_TO_GREEK = {
    " ": " ", #for spaces to work
    ",": ",", #for commas to work
    "a": "α",
    "b": "β",
    "g": "γ",
    "d": "δ",
    "e": "ε",
    "ai": "αι",
    "z": "ζ",
    "i": "ι",
    "h": "η",
    "ei": "ει",
    "oi": "οι",
    "th": "θ",
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
    "ch": "χ",
    "ps": "ψ"
}

GREEKLISH_TO_GREEK_CAPITALS = {k.upper():v.upper() for k,v in GREEKLISH_TO_GREEK.items()}

#Check Input
if len(sys.argv) < 2:
    string = input("Type the sentence in greeklish:\n")
else:
    string = str(sys.argv[1])

converted_string = ""

#Convert uppercase
for capital_letter in string:
    if str(capital_letter) in GREEKLISH_CHARS_CAPITALS:
        capital_letter = capital_letter.replace(capital_letter, GREEKLISH_TO_GREEK_CAPITALS[capital_letter])
        converted_string += capital_letter
#Convert lowercase
for letter in string:
    if str(letter) in GREEKLISH_CHARS:
        letter = letter.replace(letter, GREEKLISH_TO_GREEK[letter])
        converted_string += letter
#Convert symbols
for symbol in string:
    if str(symbol) == "?":
        symbol = symbol.replace("?", ";")
        converted_string += symbol


uppers = [upper for upper in string if letter.isupper()]
lowers = [lower for lower in string if letter.islower()]


#Convert lowercase doubles
if "πσ" in converted_string:
    converted_string = converted_string.replace("πσ", "ψ")

if "κσ" in converted_string:
    converted_string = converted_string.replace("κσ", "ξ")

if "τη" in converted_string:
    converted_string = converted_string.replace("τη", "θ")
#Convert UPPERCASE doubles
if "ΠΣ" in converted_string:
    converted_string = converted_string.replace("ΠΣ", "Ψ")

if "ΚΣ" in converted_string:
    converted_string = converted_string.replace("ΚΣ", "Ξ")

if "ΤΗ" in converted_string:
    converted_string = converted_string.replace("ΤΗ", "Θ")

#Convert σ to ς at the end of every word
converted_string_words = converted_string.split(" ")
while '' in converted_string_words:
    converted_string_words.remove('')

for word in converted_string_words:
    if word[-1] == 'σ':
        converted_string_words.remove(word)
        word = word[:-1] + "ς"
        converted_string_words.append(word)


print(" ".join(converted_string_words))
        



#TODO
#Fix bug: Capitals go first, lowercase next, symbols last.