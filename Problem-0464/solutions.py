
__problem_title__ = "MÃ¶bius function and intervals"
__problem_url___ = "https://projecteuler.net/problem=464"
__problem_description__ = "The , denoted ( ), is defined as: Let P( , ) be the number of " \
                          "integers in the interval [ , ] such that ( ) = 1. Let N( , ) be the " \
                          "number of integers in the interval [ , ] such that ( ) = -1. For " \
                          "example, P(2,10) = 2 and N(2,10) = 4. Let C( ) be the number of " \
                          "integer pairs ( , ) such that: For example, C(10) = 13, C(500) = " \
                          "16676 and C(10 000) = 20155319. Find C(20 000 000)."

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

