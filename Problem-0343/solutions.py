
__problem_title__ = "Fractional Sequences"
__problem_url___ = "https://projecteuler.net/problem=343"
__problem_description__ = "For any positive integer , a finite sequence a of fractions x /y is " \
                          "defined by: a = 1/ and a = (x +1)/(y -1) reduced to lowest terms for " \
                          ">1. When a reaches some integer , the sequence stops. (That is, when " \
                          "y =1.) Define f( ) = . For example, for = 20: 1/20 → 2/19 → 3/18 = " \
                          "1/6 → 2/5 → 3/4 → 4/3 → 5/2 → 6/1 = 6 So f(20) = 6. Also f(1) = 1, " \
                          "f(2) = 2, f(3) = 1 and Σf( ) = 118937 for 1 ≤ ≤ 100. Find Σf( ) for 1 " \
                          "≤ ≤ 2×10 ."

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

