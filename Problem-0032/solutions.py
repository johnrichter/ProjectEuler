
__problem_title__ = "Pandigital products"
__problem_url___ = "https://projecteuler.net/problem=32"
__problem_description__ = "We shall say that an -digit number is pandigital if it makes use of " \
                          "all the digits 1 to exactly once; for example, the 5-digit number, " \
                          "15234, is 1 through 5 pandigital. The product 7254 is unusual, as the " \
                          "identity, 39 × 186 = 7254, containing multiplicand, multiplier, and " \
                          "product is 1 through 9 pandigital. Find the sum of all products whose " \
                          "multiplicand/multiplier/product identity can be written as a 1 " \
                          "through 9 pandigital."

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

