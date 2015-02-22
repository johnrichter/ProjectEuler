
__problem_title__ = "Four Representations using Squares"
__problem_url___ = "https://projecteuler.net/problem=229"
__problem_description__ = "Consider the number 3600. It is very special, because Similarly, we " \
                          "find that 88201 = 99 + 280 = 287 + 2×54 = 283 + 3×52 = 197 + 7×84 . " \
                          "In 1747, Euler proved which numbers are representable as a sum of two " \
                          "squares. We are interested in the numbers which admit representations " \
                          "of all of the following four types: where the and are positive " \
                          "integers. There are 75373 such numbers that do not exceed 10 . How " \
                          "many such numbers are there that do not exceed 2×10 ?"

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

