
__problem_title__ = "A polynomial modulo the square of a prime"
__problem_url___ = "https://projecteuler.net/problem=457"
__problem_description__ = "Let ( ) = - 3 - 1. Let be a prime. Let R( ) be the smallest positive " \
                          "integer such that ( ) mod p = 0 if such an integer exists, otherwise " \
                          "R( ) = 0. Let SR( ) be &Sum;R( ) for all primes not exceeding . Find " \
                          "SR(10 )."

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

