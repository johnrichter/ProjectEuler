
__problem_title__ = "Circle and tangent line"
__problem_url___ = "https://projecteuler.net/problem=410"
__problem_description__ = "Let C be the circle with radius , + = . We choose two points P( , ) " \
                          "and Q(- , ) so that the line passing through P and Q is tangent to C. " \
                          "For example, the quadruplet ( , , , ) = (2, 6, 2, -7) satisfies this " \
                          "property. Let F( , ) be the number of the integer quadruplets ( , , , " \
                          ") with this property, and with 0 < ≤ and 0 < ≤ . We can verify that " \
                          "F(1, 5) = 10, F(2, 10) = 52 and F(10, 100) = 3384. Find F(10 , 10 ) + " \
                          "F(10 , 10 )."

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

