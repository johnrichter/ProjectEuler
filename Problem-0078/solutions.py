
__problem_title__ = "Coin partitions"
__problem_url___ = "https://projecteuler.net/problem=78"
__problem_description__ = "Let p( ) represent the number of different ways in which coins can be " \
                          "separated into piles. For example, five coins can separated into " \
                          "piles in exactly seven different ways, so p(5)=7. Find the least " \
                          "value of for which p( ) is divisible by one million."

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

