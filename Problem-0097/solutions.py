
__problem_title__ = "Large non-Mersenne prime"
__problem_url___ = "https://projecteuler.net/problem=97"
__problem_description__ = "The first known prime found to exceed one million digits was " \
                          "discovered in 1999, and is a Mersenne prime of the form 2 −1; it " \
                          "contains exactly 2,098,960 digits. Subsequently other Mersenne " \
                          "primes, of the form 2 −1, have been found which contain more digits. " \
                          "However, in 2004 there was found a massive non-Mersenne prime which " \
                          "contains 2,357,207 digits: 28433×2 +1. Find the last ten digits of " \
                          "this prime number."

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

