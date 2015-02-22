
__problem_title__ = "Largest roots of cubic polynomials"
__problem_url___ = "https://projecteuler.net/problem=356"
__problem_description__ = "Let be the largest real root of a polynomial (x) = x - 2 ·x + . For " \
                          "example, = 3.86619826... Find the last eight digits of . : represents " \
                          "the floor function."

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

