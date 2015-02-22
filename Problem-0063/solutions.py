
__problem_title__ = "Powerful digit counts"
__problem_url___ = "https://projecteuler.net/problem=63"
__problem_description__ = "The 5-digit number, 16807=7 , is also a fifth power. Similarly, the " \
                          "9-digit number, 134217728=8 , is a ninth power. How many -digit " \
                          "positive integers exist which are also an th power?"

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

