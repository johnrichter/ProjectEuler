
__problem_title__ = "Modified Fibonacci golden nuggets"
__problem_url___ = "https://projecteuler.net/problem=140"
__problem_description__ = "Consider the infinite polynomial series A ( ) = G + G + G + ..., " \
                          "where G is the th term of the second order recurrence relation G = G " \
                          "+ G , G = 1 and G = 4; that is, 1, 4, 5, 9, 14, 23, ... . For this " \
                          "problem we shall be concerned with values of for which A ( ) is a " \
                          "positive integer. The corresponding values of for the first five " \
                          "natural numbers are shown below. We shall call A ( ) a golden nugget " \
                          "if is rational, because they become increasingly rarer; for example, " \
                          "the 20th golden nugget is 211345365. Find the sum of the first thirty " \
                          "golden nuggets."

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

