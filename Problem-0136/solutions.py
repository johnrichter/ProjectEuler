
__problem_title__ = "Singleton difference"
__problem_url___ = "https://projecteuler.net/problem=136"
__problem_description__ = "The positive integers, , , and , are consecutive terms of an " \
                          "arithmetic progression. Given that is a positive integer, the " \
                          "equation, − − = , has exactly one solution when = 20: 13 − 10 − 7 = " \
                          "20 In fact there are twenty-five values of below one hundred for " \
                          "which the equation has a unique solution. How many values of less " \
                          "than fifty million have exactly one solution?"

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

