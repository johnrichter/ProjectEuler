
__problem_title__ = "Spiral primes"
__problem_url___ = "https://projecteuler.net/problem=58"
__problem_description__ = "Starting with 1 and spiralling anticlockwise in the following way, a " \
                          "square spiral with side length 7 is formed. 36 35 34 33 32 38 16 15 " \
                          "14 30 39 18 4 12 29 40 19 6 1 2 11 28 41 20 8 9 10 27 42 21 22 23 24 " \
                          "25 26 44 45 46 47 48 49 It is interesting to note that the odd " \
                          "squares lie along the bottom right diagonal, but what is more " \
                          "interesting is that 8 out of the 13 numbers lying along both " \
                          "diagonals are prime; that is, a ratio of 8/13 ≈ 62%. If one complete " \
                          "new layer is wrapped around the spiral above, a square spiral with " \
                          "side length 9 will be formed. If this process is continued, what is " \
                          "the side length of the square spiral for which the ratio of primes " \
                          "along both diagonals first falls below 10%?"

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

