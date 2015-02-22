
__problem_title__ = "Sum of squares of unitary divisors"
__problem_url___ = "https://projecteuler.net/problem=429"
__problem_description__ = "A unitary divisor of a number is a divisor of that has the property " \
                          "gcd( ) = 1. The unitary divisors of 4! = 24 are 1, 3, 8 and 24. The " \
                          "sum of their squares is 1 + 3 + 8 + 24 = 650. Let S( ) represent the " \
                          "sum of the squares of the unitary divisors of . Thus S(4!)=650. Find " \
                          "S(100 000 000!) modulo 1 000 000 009."

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

