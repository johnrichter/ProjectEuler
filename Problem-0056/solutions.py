
__problem_title__ = "Powerful digit sum"
__problem_url___ = "https://projecteuler.net/problem=56"
__problem_description__ = "A googol (10 ) is a massive number: one followed by one-hundred " \
                          "zeros; 100 is almost unimaginably large: one followed by two-hundred " \
                          "zeros. Despite their size, the sum of the digits in each number is " \
                          "only 1. Considering natural numbers of the form, , where < 100, what " \
                          "is the maximum digital sum?"

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

