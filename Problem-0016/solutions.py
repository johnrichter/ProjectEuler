
__problem_title__ = "Power digit sum"
__problem_url___ = "https://projecteuler.net/problem=16"
__problem_description__ = "2 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26. What " \
                          "is the sum of the digits of the number 2 ?"

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

