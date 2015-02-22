
__problem_title__ = "Summation of primes"
__problem_url___ = "https://projecteuler.net/problem=10"
__problem_description__ = "The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of " \
                          "all the primes below two million."

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

