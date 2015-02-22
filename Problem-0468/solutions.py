
__problem_title__ = "Smooth divisors of binomial coefficients"
__problem_url___ = "https://projecteuler.net/problem=468"
__problem_description__ = "An integer is called if none of its prime factors is greater than . " \
                          "Let S ( ) be the largest -smooth divisor of . Examples: S (10) = 1 S " \
                          "(2100) = 12 S (2496144) = 5712 Define F( ) = ∑ ∑ S (C( , )). Here, C( " \
                          ", ) denotes the binomial coefficient. Examples: F(11) = 3132 F(1 111) " \
                          "mod 1 000 000 993 = 706036312 F(111 111) mod 1 000 000 993 = 22156169 " \
                          "Find F(11 111 111) mod 1 000 000 993."

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

