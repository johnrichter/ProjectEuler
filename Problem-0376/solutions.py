
__problem_title__ = "Nontransitive sets of dice"
__problem_url___ = "https://projecteuler.net/problem=376"
__problem_description__ = "Consider the following set of dice with nonstandard pips: Die A: 1 4 " \
                          "4 4 4 4 Die B: 2 2 2 5 5 5 Die C: 3 3 3 3 3 6 A game is played by two " \
                          "players picking a die in turn and rolling it. The player who rolls " \
                          "the highest value wins. If the first player picks die A and the " \
                          "second player picks die B we get P(second player wins) = / > / If the " \
                          "first player picks die B and the second player picks die C we get " \
                          "P(second player wins) = / > / If the first player picks die C and the " \
                          "second player picks die A we get P(second player wins) = / > / So " \
                          "whatever die the first player picks, the second player can pick " \
                          "another die and have a larger than 50% chance of winning. A set of " \
                          "dice having this property is called a . We wish to investigate how " \
                          "many sets of nontransitive dice exist. We will assume the following " \
                          "conditions: For = 7 we find there are 9780 such sets. How many are " \
                          "there for = 30 ?"

import timeit


class Solution():

    @staticmethod
    def solution1():
        pass

    @staticmethod
    def time_solutions():
        setup = 'from __main__ import Solution'
        print('Solution 1:', timeit.timeit('Solution.solution1()', setup=setup, number=1))


if __name__ == '__main__':
    s = Solution()
    print(s.solution1())
    s.time_solutions()

