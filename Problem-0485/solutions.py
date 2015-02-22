
__problem_title__ = "Maximum number of divisors"
__problem_url___ = "https://projecteuler.net/problem=485"
__problem_description__ = "Let d(n) be the number of divisors of n. Let M(n,k) be the maximum " \
                          "value of d(j) for n ≤ j ≤ n+k-1. Let S(u,k) be the sum of M(n,k) for " \
                          "1 ≤ n ≤ u-k+1. You are given that S(1000,10)=17176. Find S(100 000 " \
                          "000,100 000)."

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

