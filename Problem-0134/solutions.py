
__problem_title__ = "Prime pair connection"
__problem_url___ = "https://projecteuler.net/problem=134"
__problem_description__ = "Consider the consecutive primes = 19 and = 23. It can be verified " \
                          "that 1219 is the smallest number such that the last digits are formed " \
                          "by whilst also being divisible by . In fact, with the exception of = " \
                          "3 and = 5, for every pair of consecutive primes, > , there exist " \
                          "values of for which the last digits are formed by and is divisible by " \
                          ". Let be the smallest of these values of . Find ∑ for every pair of " \
                          "consecutive primes with 5 ≤ ≤ 1000000."

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

