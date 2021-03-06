
__problem_title__ = "Non-abundant sums"
__problem_url___ = "https://projecteuler.net/problem=23"
__problem_description__ = "A perfect number is a number for which the sum of its proper divisors " \
                          "is exactly equal to the number. For example, the sum of the proper " \
                          "divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 " \
                          "is a perfect number. A number is called deficient if the sum of its " \
                          "proper divisors is less than and it is called abundant if this sum " \
                          "exceeds . As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = " \
                          "16, the smallest number that can be written as the sum of two " \
                          "abundant numbers is 24. By mathematical analysis, it can be shown " \
                          "that all integers greater than 28123 can be written as the sum of two " \
                          "abundant numbers. However, this upper limit cannot be reduced any " \
                          "further by analysis even though it is known that the greatest number " \
                          "that cannot be expressed as the sum of two abundant numbers is less " \
                          "than this limit. Find the sum of all the positive integers which " \
                          "cannot be written as the sum of two abundant numbers."

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

