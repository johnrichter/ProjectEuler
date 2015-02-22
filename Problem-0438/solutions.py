
__problem_title__ = "Integer part of polynomial equation's solutions"
__problem_url___ = "https://projecteuler.net/problem=438"
__problem_description__ = "For an -tuple of integers = ( , ..., ), let ( , ..., ) be the " \
                          "solutions of the polynomial equation + + + ... + + = 0. Consider the " \
                          "following two conditions: In the case of = 4, there are 12 -tuples of " \
                          "integers which satisfy both conditions. We define S( ) as the sum of " \
                          "the absolute values of the integers in . For = 4 we can verify that " \
                          "∑S( ) = 2087 for all -tuples which satisfy both conditions. Find ∑S( " \
                          ") for = 7."

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

