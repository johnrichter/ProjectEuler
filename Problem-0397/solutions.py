
__problem_title__ = "Triangle on parabola"
__problem_url___ = "https://projecteuler.net/problem=397"
__problem_description__ = "On the parabola = / , three points A( , / ), B( , / ) and C( , / ) " \
                          "are chosen. Let F( , ) be the number of the integer quadruplets ( , , " \
                          ", ) such that at least one angle of the triangle ABC is 45-degree, " \
                          "with 1 ≤ ≤ and - ≤ < < ≤ . For example, F(1, 10) = 41 and F(10, 100) " \
                          "= 12492. Find F(10 , 10 )."

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

