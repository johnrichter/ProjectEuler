
__problem_title__ = "Divisibility Multipliers"
__problem_url___ = "https://projecteuler.net/problem=274"
__problem_description__ = "For each integer > 1 coprime to 10 there is a positive < which " \
                          "preserves divisibility by for the following function on any positive " \
                          "integer, : ( ) = (all but the last digit of ) + (the last digit of ) " \
                          "* That is, if is the divisibility multiplier for , then ( ) is " \
                          "divisible by if and only if is divisible by . (When is much larger " \
                          "than , ( ) will be less than and repeated application of provides a " \
                          "multiplicative divisibility test for .) For example, the divisibility " \
                          "multiplier for 113 is 34. (76275) = 7627 + 5 * 34 = 7797 : 76275 and " \
                          "7797 are both divisible by 113 (12345) = 1234 + 5 * 34 = 1404 : 12345 " \
                          "and 1404 are both not divisible by 113 The sum of the divisibility " \
                          "multipliers for the primes that are coprime to 10 and less than 1000 " \
                          "is 39517. What is the sum of the divisibility multipliers for the " \
                          "primes that are coprime to 10 and less than 10 ?"

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

