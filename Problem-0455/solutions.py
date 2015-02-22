
__problem_title__ = "Powers With Trailing Digits"
__problem_url___ = "https://projecteuler.net/problem=455"
__problem_description__ = "Let f(n) be the largest positive integer x less than 10 such that the " \
                          "last 9 digits of n form the number (including leading zeros), or zero " \
                          "if no such integer exists. For example: Find Σf(n), 2 ≤ n ≤ 10 ."

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

