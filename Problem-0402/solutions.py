
__problem_title__ = "Integer-valued polynomials"
__problem_url___ = "https://projecteuler.net/problem=402"
__problem_description__ = "It can be shown that the polynomial + 4 + 2 + 5 is a multiple of 6 " \
                          "for every integer . It can also be shown that 6 is the largest " \
                          "integer satisfying this property. Define M( , , ) as the maximum such " \
                          "that + + + is a multiple of for all integers . For example, M(4, 2, " \
                          "5) = 6. Also, define S( ) as the sum of M( , , ) for all 0 < , , ≤ . " \
                          "We can verify that S(10) = 1972 and S(10000) = 2024258331114. Let F " \
                          "be the Fibonacci sequence: F = 0, F = 1 and F = F + F for ≥ 2. Find " \
                          "the last 9 digits of Σ S(F ) for 2 ≤ ≤ 1234567890123."

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

