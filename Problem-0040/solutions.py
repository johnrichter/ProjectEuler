
__problem_title__ = "Champernowne's constant"
__problem_url___ = "https://projecteuler.net/problem=40"
__problem_description__ = "An irrational decimal fraction is created by concatenating the " \
                          "positive integers: 0.12345678910 112131415161718192021... It can be " \
                          "seen that the 12 digit of the fractional part is 1. If represents the " \
                          "digit of the fractional part, find the value of the following " \
                          "expression. × × × × × ×"

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

