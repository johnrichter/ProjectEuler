
__problem_title__ = "Coin sums"
__problem_url___ = "https://projecteuler.net/problem=31"
__problem_description__ = "In England the currency is made up of pound, £, and pence, p, and " \
                          "there are eight coins in general circulation: It is possible to make " \
                          "£2 in the following way: How many different ways can £2 be made using " \
                          "any number of coins?"

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

