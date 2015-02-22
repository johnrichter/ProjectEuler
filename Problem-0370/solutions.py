
__problem_title__ = "Geometric triangles"
__problem_url___ = "https://projecteuler.net/problem=370"
__problem_description__ = "Let us define a as an integer sided triangle with sides ≤ ≤ so that " \
                          "its sides form a , i.e. = · . An example of such a geometric triangle " \
                          "is the triangle with sides = 144, = 156 and = 169. There are 861805 " \
                          "geometric triangles with perimeter ≤ 10 . How many geometric " \
                          "triangles exist with perimeter ≤ 2.5·10 ?"

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

