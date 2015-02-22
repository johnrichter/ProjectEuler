
__problem_title__ = "Digit fifth powers"
__problem_url___ = "https://projecteuler.net/problem=30"
__problem_description__ = "Surprisingly there are only three numbers that can be written as the " \
                          "sum of fourth powers of their digits: As 1 = 1 is not a sum it is not " \
                          "included. The sum of these numbers is 1634 + 8208 + 9474 = 19316. " \
                          "Find the sum of all the numbers that can be written as the sum of " \
                          "fifth powers of their digits."

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

