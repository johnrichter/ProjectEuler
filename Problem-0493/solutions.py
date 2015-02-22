
__problem_title__ = "Under The Rainbow"
__problem_url___ = "https://projecteuler.net/problem=493"
__problem_description__ = "70 colored balls are placed in an urn, 10 for each of the seven " \
                          "rainbow colors. What is the expected number of distinct colors in 20 " \
                          "randomly picked balls? Give your answer with nine digits after the " \
                          "decimal point (a.bcdefghij)."

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

