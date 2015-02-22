
__problem_title__ = "Same differences"
__problem_url___ = "https://projecteuler.net/problem=135"
__problem_description__ = "Given the positive integers, , , and , are consecutive terms of an " \
                          "arithmetic progression, the least value of the positive integer, , " \
                          "for which the equation, − − = , has exactly two solutions is = 27: 34 " \
                          "− 27 − 20 = 12 − 9 − 6 = 27 It turns out that = 1155 is the least " \
                          "value which has exactly ten solutions. How many values of less than " \
                          "one million have exactly ten distinct solutions?"

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

