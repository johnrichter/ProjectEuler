
__problem_title__ = "Pivotal Square Sums"
__problem_url___ = "https://projecteuler.net/problem=261"
__problem_description__ = "Let us call a positive integer a , if there is a pair of integers > 0 " \
                          "and ≥ , such that the sum of the ( +1) consecutive squares up to " \
                          "equals the sum of the consecutive squares from ( +1) on: Some small " \
                          "square-pivots are Find the sum of all square-pivots ≤ 10 ."

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

