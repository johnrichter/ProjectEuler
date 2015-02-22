
__problem_title__ = "Pandigital Fibonacci ends"
__problem_url___ = "https://projecteuler.net/problem=104"
__problem_description__ = "The Fibonacci sequence is defined by the recurrence relation: It " \
                          "turns out that F , which contains 113 digits, is the first Fibonacci " \
                          "number for which the last nine digits are 1-9 pandigital (contain all " \
                          "the digits 1 to 9, but not necessarily in order). And F , which " \
                          "contains 575 digits, is the first Fibonacci number for which the " \
                          "first nine digits are 1-9 pandigital. Given that F is the first " \
                          "Fibonacci number for which the first nine digits AND the last nine " \
                          "digits are 1-9 pandigital, find ."

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

