
__problem_title__ = "Lattice points on a circle"
__problem_url___ = "https://projecteuler.net/problem=233"
__problem_description__ = "Let ( ) be the number of points with integer coordinates that are on " \
                          "a circle passing through (0,0), ( ,0),(0, ), and ( , ). It can be " \
                          "shown that (10000) = 36. What is the sum of all positive integers ≤ " \
                          "10 such that ( ) = 420 ?"

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

