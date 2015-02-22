
__problem_title__ = "Large sum"
__problem_url___ = "https://projecteuler.net/problem=13"
__problem_description__ = "Work out the first ten digits of the sum of the following one-hundred " \
                          "50-digit numbers."

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

