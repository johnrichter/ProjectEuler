
__problem_title__ = "Totient Chains"
__problem_url___ = "https://projecteuler.net/problem=214"
__problem_description__ = "Let φ be Euler's totient function, i.e. for a natural number , φ( ) " \
                          "is the number of , 1 ≤ ≤ , for which gcd( , ) = 1. By iterating φ, " \
                          "each positive integer generates a decreasing chain of numbers ending " \
                          "in 1. E.g. if we start with 5 the sequence 5,4,2,1 is generated. Here " \
                          "is a listing of all chains with length 4: Only two of these chains " \
                          "start with a prime, their sum is 12. What is the sum of all primes " \
                          "less than 40000000 which generate a chain of length 25?"

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

