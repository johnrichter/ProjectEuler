
__problem_title__ = "Remainder of polynomial division"
__problem_url___ = "https://projecteuler.net/problem=498"
__problem_description__ = "For positive integers and , we define two polynomials F ( ) = and G ( " \
                          ") = ( -1) . We also define a polynomial R ( ) as the remainder of the " \
                          "division of F ( ) by G ( ). For example, R ( ) = 15 - 24 + 10. Let C( " \
                          ", , ) be the absolute value of the coefficient of the -th degree term " \
                          "of R ( ). We can verify that C(6, 3, 1) = 24 and C(100, 10, 4) = " \
                          "227197811615775. Find C(10 , 10 , 10 ) mod 999999937."

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

