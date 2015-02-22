
__problem_title__ = "Counting fractions"
__problem_url___ = "https://projecteuler.net/problem=72"
__problem_description__ = "Consider the fraction, , where and are positive integers. If < and " \
                          "HCF( )=1, it is called a reduced proper fraction. If we list the set " \
                          "of reduced proper fractions for ≤ 8 in ascending order of size, we " \
                          "get: 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, " \
                          "5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8 It can be seen that there are " \
                          "21 elements in this set. How many elements would be contained in the " \
                          "set of reduced proper fractions for ≤ 1,000,000?"

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

