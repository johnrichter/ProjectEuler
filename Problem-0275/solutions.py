
__problem_title__ = "Balanced Sculptures"
__problem_url___ = "https://projecteuler.net/problem=275"
__problem_description__ = "Let us define a of order as follows: When counting the sculptures, " \
                          "any arrangements which are simply reflections about the -axis, are " \
                          "counted as distinct. For example, the 18 balanced sculptures of order " \
                          "6 are shown below; note that each pair of mirror images (about the " \
                          "-axis) is counted as one sculpture: There are 964 balanced sculptures " \
                          "of order 10 and 360505 of order 15. How many balanced sculptures are " \
                          "there of order 18?"

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

