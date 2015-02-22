
__problem_title__ = "Fibonacci golden nuggets"
__problem_url___ = "https://projecteuler.net/problem=137"
__problem_description__ = "Consider the infinite polynomial series A ( ) = F + F + F + ..., " \
                          "where F is the th term in the Fibonacci sequence: 1, 1, 2, 3, 5, 8, " \
                          "... ; that is, F = F + F , F = 1 and F = 1. For this problem we shall " \
                          "be interested in values of for which A ( ) is a positive integer. The " \
                          "corresponding values of for the first five natural numbers are shown " \
                          "below. We shall call A ( ) a golden nugget if is rational, because " \
                          "they become increasingly rarer; for example, the 10th golden nugget " \
                          "is 74049690. Find the 15th golden nugget."

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

