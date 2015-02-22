
__problem_title__ = "Pseudo Square Root"
__problem_url___ = "https://projecteuler.net/problem=266"
__problem_description__ = "The divisors of 12 are: 1,2,3,4,6 and 12. The largest divisor of 12 " \
                          "that does not exceed the square root of 12 is 3. We shall call the " \
                          "largest divisor of an integer that does not exceed the square root of " \
                          "the pseudo square root (PSR) of . It can be seen that PSR(3102)=47. " \
                          "Let be the product of the primes below 190. Find PSR( ) mod 10 ."

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

