
__problem_title__ = "Special isosceles triangles"
__problem_url___ = "https://projecteuler.net/problem=138"
__problem_description__ = "Consider the isosceles triangle with base length, = 16, and legs, L = " \
                          "17. By using the Pythagorean theorem it can be seen that the height " \
                          "of the triangle, = √(17 − 8 ) = 15, which is one less than the base " \
                          "length. With = 272 and L = 305, we get = 273, which is one more than " \
                          "the base length, and this is the second smallest isosceles triangle " \
                          "with the property that = ± 1. Find ∑ L for the twelve smallest " \
                          "isosceles triangles for which = ± 1 and , L are positive integers."

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

