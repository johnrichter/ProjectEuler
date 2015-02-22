
__problem_title__ = "GCD sequence"
__problem_url___ = "https://projecteuler.net/problem=443"
__problem_description__ = "Let g( ) be a sequence defined as follows: g(4) = 13, g( ) = g( -1) + " \
                          "gcd( , g( -1)) for > 4. The first few values are: You are given that " \
                          "g(1 000) = 2524 and g(1 000 000) = 2624152. Find g(10 )."

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

