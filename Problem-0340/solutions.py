
__problem_title__ = "Crazy Function"
__problem_url___ = "https://projecteuler.net/problem=340"
__problem_description__ = "For fixed integers a, b, c, define the F( ) as follows: F( ) = - c " \
                          "for all > b F( ) = F(a + F(a + F(a + F(a + )))) for all ≤ b. Also, " \
                          "define S(a, b, c) = . For example, if a = 50, b = 2000 and c = 40, " \
                          "then F(0) = 3240 and F(2000) = 2040. Also, S(50, 2000, 40) = 5204240. " \
                          "Find the last 9 digits of S(21 , 7 , 12 )."

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

