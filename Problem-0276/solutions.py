
__problem_title__ = "Primitive Triangles"
__problem_url___ = "https://projecteuler.net/problem=276"
__problem_description__ = "Consider the triangles with integer sides a, b and c with a ≤ b ≤ c. " \
                          "An integer sided triangle (a,b,c) is called primitive if =1. How many " \
                          "primitive integer sided triangles exist with a perimeter not " \
                          "exceeding 10 000 000?"

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

