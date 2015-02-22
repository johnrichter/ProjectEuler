
__problem_title__ = "Finding numbers for which the sum of the squares of the digits is a square"
__problem_url___ = "https://projecteuler.net/problem=171"
__problem_description__ = "For a positive integer , let f( ) be the sum of the squares of the " \
                          "digits (in base 10) of , e.g. f(3) = 3 = 9, f(25) = 2 + 5 = 4 + 25 = " \
                          "29, f(442) = 4 + 4 + 2 = 16 + 16 + 4 = 36 Find the last nine digits " \
                          "of the sum of all , 0 < < 10 , such that f( ) is a perfect square."

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

