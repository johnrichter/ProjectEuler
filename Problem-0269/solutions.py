
__problem_title__ = "Polynomials with at least one integer root"
__problem_url___ = "https://projecteuler.net/problem=269"
__problem_description__ = "A root or zero of a polynomial P( ) is a solution to the equation P( " \
                          ") = 0. Define P as the polynomial whose coefficients are the digits " \
                          "of . For example, P ( ) = 5 + 7 + 3. We can see that: Define Z( ) as " \
                          "the number of positive integers, , not exceeding for which the " \
                          "polynomial P has at least one integer root. It can be verified that " \
                          "Z(100 000) is 14696. What is Z(10 )?"

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

