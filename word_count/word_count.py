#!/usr/bin/env python3
import sys
import re


def line_count(text):
    return len(text.splitlines())


def word_count(text):
    return len(text.split())


def char_count(text):
    return len(text)


def counts(text, flags):
    return dict(
        l=line_count(text) if "l" in flags else None,
        w=word_count(text) if "w" in flags else None,
        c=char_count(text) if "c" in flags else None,
    )


def total_counts(file_counts, flags):
    total = dict(l=0,w=0,c=0)

    for filename, counts in file_counts.items():
        for field, value in counts.items():
            if field in flags:
                total[field] += value

    return total


def print_counts(counts, flags, description=""):
    l = f"{counts['l']:>8}" if "l" in flags else ""
    w = f"{counts['w']:>8}" if "w" in flags else ""
    c = f"{counts['c']:>8}" if "c" in flags else ""
    print(f"{l}{w}{c} {description}")


def parse():
    import argparse

    parser = argparse.ArgumentParser(
        prog="word_count",
        allow_abbrev=False,
        description="Print newline, word, and byte counts for each FILE",
    )
    # fmt: off
    parser.add_argument( "-l", "--lines", action="append_const", const="l", dest="flags", help="print the newline counts")
    parser.add_argument( "-w", "--words", action="append_const", const="w", dest="flags", help="print the word counts")
    parser.add_argument( "-c", "--chars", action="append_const", const="c", dest="flags", help="print the character counts")
    parser.add_argument("filenames", action="store", nargs="*", metavar="FILE")
    # fmt: on

    args = parser.parse_args()
    filenames = args.filenames or [""]
    flags = set(args.flags or "lwc")
    return (filenames, flags)


def main():
    filenames, flags = parse()
    file_counts = {}

    for filename in filenames:
        try:
            with sys.stdin if filename in ["-", ""] else open(filename) as file:
                text = file.read()
                file_counts[filename] = counts(text, flags)
                print_counts(file_counts[filename], flags, filename)
        except OSError as err:
            print(f"{err.filename}: {err.strerror}")

    if len(file_counts) > 1:
        _total_counts = total_counts(file_counts, flags)
        print_counts(_total_counts, flags, "total")


if __name__ == "__main__":
    main()
