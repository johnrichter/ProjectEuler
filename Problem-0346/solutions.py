
__problem_title__ = "Strong Repunits"
__problem_url___ = "https://projecteuler.net/problem=346"
__problem_description__ = "The number 7 is special, because 7 is 111 written in base 2, and 11 " \
                          "written in base 6 (i.e. 7 = 11 = 111 ). In other words, 7 is a " \
                          "repunit in at least two bases b > 1. We shall call a positive integer " \
                          "with this property a strong repunit. It can be verified that there " \
                          "are 8 strong repunits below 50: {1,7,13,15,21,31,40,43}. Furthermore, " \
                          "the sum of all strong repunits below 1000 equals 15864."

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

