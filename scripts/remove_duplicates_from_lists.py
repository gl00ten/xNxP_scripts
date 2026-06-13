#!/usr/bin/env python3
"""Remove common elements between two lists.

Returns (only_in_1, only_in_2, intersection) as sorted lists.

Can be used as library:
  from remove_duplicates_from_lists import removedups
"""

import argparse
import sys
from typing import List, Tuple


def removedups(list1: List[str], list2: List[str]) -> Tuple[List[str], List[str], List[str]]:
    set1, set2 = set(list1), set(list2)
    common = set1 & set2
    return sorted(set1 - common), sorted(set2 - common), sorted(common)


def main():
    parser = argparse.ArgumentParser(description="Set difference between two lists of strings")
    parser.add_argument("file1", help="File with one item per line (list A)")
    parser.add_argument("file2", help="File with one item per line (list B)")
    args = parser.parse_args()

    try:
        with open(args.file1) as f:
            a = [line.rstrip("\n") for line in f]
        with open(args.file2) as f:
            b = [line.rstrip("\n") for line in f]
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)

    only_a, only_b, common = removedups(a, b)
    print("=== only in", args.file1)
    print("\n".join(only_a) or "(none)")
    print("\n=== only in", args.file2)
    print("\n".join(only_b) or "(none)")
    print("\n=== common")
    print("\n".join(common) or "(none)")


if __name__ == "__main__":
    main()
