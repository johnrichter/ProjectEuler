
__problem_title__ = "A lagged Fibonacci sequence"
__problem_url___ = "https://projecteuler.net/problem=258"
__problem_description__ = "A sequence is defined as: Find mod 20092010 for = 10 ."

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

