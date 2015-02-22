
__problem_title__ = "Factorial digit sum"
__problem_url___ = "https://projecteuler.net/problem=20"
__problem_description__ = "! means × ( − 1) × ... × 3 × 2 × 1 For example, 10! = 10 × 9 × ... × " \
                          "3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is 3 " \
                          "+ 6 + 2 + 8 + 8 + 0 + 0 = 27. Find the sum of the digits in the " \
                          "number 100!"

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

