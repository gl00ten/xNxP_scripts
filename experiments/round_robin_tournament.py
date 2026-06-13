#!/usr/bin/env python3
"""Round-robin tournament fixture generator.

Produces a list of rounds where each team plays every other team exactly once.

Usage:
  python round_robin_tournament.py TeamA TeamB TeamC TeamD
  python round_robin_tournament.py --teams-file teams.txt
"""

import argparse
import random
import sys
from typing import List, Tuple


def generate_fixtures(teams: List[str]) -> List[List[Tuple[str, str]]]:
    teams = list(teams)
    if len(teams) % 2 == 1:
        teams.append("BYE")  # bye for odd count

    rotation = teams[:]
    rounds = []
    for _ in range(len(teams) - 1):
        rounds.append(rotation[:])
        rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

    # pair them up
    paired_rounds: List[List[Tuple[str, str]]] = []
    for r in rounds:
        pairs = []
        rcopy = r[:]
        while rcopy:
            a = rcopy.pop(0)
            b = rcopy.pop()
            if a == "BYE":
                pairs.append((b, "BYE"))
            elif b == "BYE":
                pairs.append((a, "BYE"))
            else:
                pairs.append((a, b))
        paired_rounds.append(pairs)

    random.shuffle(paired_rounds)
    return paired_rounds


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("teams", nargs="*", help="Team names")
    parser.add_argument("--teams-file", help="File with one team per line")
    parser.add_argument("--seed", type=int, help="Random seed for shuffle")
    args = parser.parse_args()

    if args.teams_file:
        with open(args.teams_file) as f:
            teams = [line.strip() for line in f if line.strip()]
    else:
        teams = args.teams

    if len(teams) < 2:
        parser.print_help()
        sys.exit(1)

    if args.seed is not None:
        random.seed(args.seed)

    fixtures = generate_fixtures(teams)

    print("Teams:", teams)
    print()
    for rnd_idx, rnd in enumerate(fixtures, 1):
        print(f"Round {rnd_idx}:")
        for a, b in rnd:
            if b == "BYE":
                print(f"  {a} gets a bye")
            else:
                print(f"  {a} vs {b}")
        print()


if __name__ == "__main__":
    main()
