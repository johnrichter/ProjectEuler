
__problem_title__ = "Quadratic primes"
__problem_url___ = "https://projecteuler.net/problem=27"
__problem_description__ = "Euler discovered the remarkable quadratic formula: ² + + 41 It turns " \
                          "out that the formula will produce 40 primes for the consecutive " \
                          "values = 0 to 39. However, when = 40, 40 + 40 + 41 = 40(40 + 1) + 41 " \
                          "is divisible by 41, and certainly when = 41, 41² + 41 + 41 is clearly " \
                          "divisible by 41. The incredible formula ² − 79 + 1601 was discovered, " \
                          "which produces 80 primes for the consecutive values = 0 to 79. The " \
                          "product of the coefficients, −79 and 1601, is −126479. Considering " \
                          "quadratics of the form: Find the product of the coefficients, and , " \
                          "for the quadratic expression that produces the maximum number of " \
                          "primes for consecutive values of , starting with = 0."

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

