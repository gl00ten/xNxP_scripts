#!/usr/bin/env python3
"""Human-readable text scrambler.

Keeps first and last letter of words, shuffles the middle letters.
This often remains surprisingly readable (psycholinguistics effect).

Usage:
  python scramble_text.py "your phrase here"
  echo "text" | python scramble_text.py
"""

import random
import sys


def scramble_text(phrase: str) -> str:
    words = phrase.split(' ')
    return ' '.join(_scramble_word(w) for w in words)


def _scramble_word(word: str) -> str:
    if not word:
        return word
    # preserve trailing punctuation
    suffix = ''
    for p in '.;:,!?':
        if word.endswith(p):
            suffix = p
            word = word[:-1]
            break
    if len(word) <= 3:
        return word + suffix
    middle = list(word[1:-1])
    random.shuffle(middle)
    return word[0] + ''.join(middle) + word[-1] + suffix


def main():
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        # read from stdin
        text = sys.stdin.read()
    print(scramble_text(text.rstrip('\n')))


if __name__ == '__main__':
    main()
