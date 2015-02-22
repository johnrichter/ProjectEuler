
__problem_title__ = "Repunit nonfactors"
__problem_url___ = "https://projecteuler.net/problem=133"
__problem_description__ = "A number consisting entirely of ones is called a repunit. We shall " \
                          "define R( ) to be a repunit of length ; for example, R(6) = 111111. " \
                          "Let us consider repunits of the form R(10 ). Although R(10), R(100), " \
                          "or R(1000) are not divisible by 17, R(10000) is divisible by 17. Yet " \
                          "there is no value of for which R(10 ) will divide by 19. In fact, it " \
                          "is remarkable that 11, 17, 41, and 73 are the only four primes below " \
                          "one-hundred that can be a factor of R(10 ). Find the sum of all the " \
                          "primes below one-hundred thousand that will never be a factor of R(10 " \
                          ")."

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

