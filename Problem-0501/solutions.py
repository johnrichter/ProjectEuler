
__problem_title__ = "Eight Divisors"
__problem_url___ = "https://projecteuler.net/problem=501"
__problem_description__ = "The eight divisors of 24 are 1, 2, 3, 4, 6, 8, 12 and 24. The ten " \
                          "numbers not exceeding 100 having exactly eight divisors are 24, 30, " \
                          "40, 42, 54, 56, 66, 70, 78 and 88. Let ( ) be the count of numbers " \
                          "not exceeding with exactly eight divisors. You are given (100) = 10, " \
                          "(1000) = 180 and (10 ) = 224427. Find (10 )."

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

