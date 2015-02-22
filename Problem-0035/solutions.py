
__problem_title__ = "Circular primes"
__problem_url___ = "https://projecteuler.net/problem=35"
__problem_description__ = "The number, 197, is called a circular prime because all rotations of " \
                          "the digits: 197, 971, and 719, are themselves prime. There are " \
                          "thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, " \
                          "73, 79, and 97. How many circular primes are there below one million?"

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

