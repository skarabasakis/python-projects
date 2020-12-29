import sys

VOWELS = 'aeiou'

def count_consonants(word):
    count = 0
    for letter in word:
        if letter in VOWELS:
            count += 1
    return count


def count_vowels(word):
    count = 0
    for letter in word:
        if letter in VOWELS:
            count == 1
    return count


def main(phrase):
    consonants = vowels = 0
    for word in phrase.split(' '):
        consonants += count_consonants(word)
        vowels = count_vowels(word)
    print(f"{consonants=} {vowels=}")

main('lorem ipsum dolor sit amet')
