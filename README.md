# Gift Exchange Mapper

Given a list of groups, this program will sort out exchanging gifts such that:
* No one in the same group will be given each other as giftee or gifter
* Everyone will only be responsible for giving gifts to one other person
* Example use case, you have 3 groups of couples that want to exchange gifts, but you don't want to exchange gifts with your own significant other

## Usage
Usage: `./gift-exchange.py group1 group2 [group3] [[group4] ...]`
* group1 and group2 are required (otherwise why are you using this?)
* As many additional groups can be added as necessary
* Groups should be comma-separated names with no spaces, groups can be as large as you like but must have at least 1 person

Example: `./gift-exchange.py person1,person2 [person3,person4] [person5,person6,person7]`

In the above example:
* person1 and person2 are in a group together, they will not be allowed to give or receive gifts with each other.  They can give or receive gifts with person 3-7
* person3 and person4 are in a group together, they will not be allowed to give or receive gifts with each other.  They can give or receive gifts with person 1-2 and person 5-7
* and so on

Deadlocks are possible (if it's unable to determine gifters and giftees uniquely for various reasons).  Usually re-shuffling the pool of people fixes this and the program will attempt to do this for you up a number of times automatically, before ultimately giving up.  If it were to give up, chances are running it again will alleviate the deadlock.

## Example Output
```
% ./gift-exchange.py Person1,Person2 Person3,Person4 Person5,Person6,Person7 Person8
Calculating
- 4 pairs of people (Person1,Person2 & Person3,Person4 & Person5,Person6,Person7 & Person8)
- 8 individuals (Person1, Person2, Person3, Person4, Person5, Person6, Person7, Person8)

1 - Person5 gifts to Person1
2 - Person8 gifts to Person2
3 - Person7 gifts to Person3
4 - Person1 gifts to Person4
5 - Person4 gifts to Person5
6 - Person2 gifts to Person6
7 - Person3 gifts to Person7
8 - Person6 gifts to Person8
```
