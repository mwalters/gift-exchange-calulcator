#!/usr/bin/env python3

import sys, random

version = "0.0.1"
pairs = sys.argv
pairs.pop(0)
num_pairs = len(pairs)


def print_help():
    print()
    print("Gift Exchange Mapper v{version}".format(version=version))
    print()
    print(
        "Given a list of groups, this program will sort out exchanging gifts such that:"
    )
    print("- No one in the same group will be given each other as giftee or gifter")
    print("- Everyone will only be responsible for giving gifts to one other person")
    print(
        "- Example use case, you have 3 groups of couples that want to exchange gifts, but you don't want to exchange gifts with your own significant other"
    )
    print()
    print("Usage: ./gift-exchange.py group1 group2 [group3] [[group4] ...]")
    print("- group1 and group2 are required (otherwise why are you using this?)")
    print("- As many additional groups can be added as necessary")
    print(
        "- Groups should be comma-separated names with no spaces, groups can be as large as you like but must have at least 1 person"
    )
    print()
    print(
        "Example: ./gift-exchange.py person1,person2 [person3,person4] [person5,person6,person7]"
    )
    print()
    print("In the above example:")
    print(
        "- person1 and person2 are in a group together, they will not be allowed to give or receive gifts with each other.  They can give or receive gifts with person 3-7"
    )
    print(
        "- person3 and person4 are in a group together, they will not be allowed to give or receive gifts with each other.  They can give or receive gifts with person 1-2 and person 5-7"
    )
    print("- and so on")
    print()
    print(
        "Deadlocks are possible (if it's unable to determine gifters and giftees uniquely for various reasons).  Usually re-shuffling the pool of people fixes this and the program will attempt to do this for you up to 10 times automatically."
    )
    print()


if len(pairs) == 0:
    print_help()
    exit(1)

print("Calculating ", end="")
deadlock = True
deadlock_ctr = 1
while deadlock and deadlock_ctr < 100:
    pool = {}
    gifters = []
    gift_giving = {}

    for pair in pairs:
        individuals = pair.split(",")
        for individual in individuals:
            pool[individual] = []

    if len(list(pool.keys())) < 2:
        print_help()
        exit(2)

    for x in range(0, num_pairs):
        individuals = pairs[x].split(",")
        for individual in individuals:
            for y in range(0, num_pairs):
                if x == y:
                    continue
                gifters = pairs[y].split(",")
                for gifter in gifters:
                    pool[individual].append(gifter)

    for individual in pool.keys():
        random.shuffle(pool[individual])

    gifters = []
    for individual in pool.keys():
        gifter_found = False
        while gifter_found == False:
            if len(pool[individual]) > 0:
                if pool[individual][0] not in gifters:
                    gifter_found = True
                    gifters.append(pool[individual][0])
                    gift_giving[individual] = pool[individual][0]
                else:
                    pool[individual].pop(0)
            else:
                print(".", end="")
                gifter_found = True
                deadlock_ctr = deadlock_ctr + 1
                continue
        if len(gifters) == len(list(pool.keys())):
            deadlock = False
print()
print(
    "- {num_pairs} pairs of people ({list})".format(
        num_pairs=num_pairs, list=" & ".join(pairs)
    )
)
print(
    "- {num_individuals} individuals ({list})".format(
        num_individuals=len(list(pool.keys())), list=", ".join(list(pool.keys()))
    )
)
print()

i = 0
for giftee in gift_giving.keys():
    i += 1
    print(
        "{ctr} - {gifter} gifts to {giftee}".format(
            ctr=i, gifter=gift_giving[giftee].capitalize(), giftee=giftee.capitalize()
        )
    )
