
__problem_title__ = "Circular Logic"
__problem_url___ = "https://projecteuler.net/problem=209"
__problem_description__ = "A -input is a map from input bits (binary digits, 0 [false] or 1 " \
                          "[true]) to 1 output bit. For example, the 2-input binary truth tables " \
                          "for the logical AND and XOR functions are: How many 6-input binary " \
                          "truth tables, τ, satisfy the formula for all 6-bit inputs ( , , , , , " \
                          ")?"

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

