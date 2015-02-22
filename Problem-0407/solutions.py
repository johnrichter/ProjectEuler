
__problem_title__ = "Idempotents"
__problem_url___ = "https://projecteuler.net/problem=407"
__problem_description__ = "If we calculate mod 6 for 0 ≤ ≤ 5 we get: 0,1,4,3,4,1. The largest " \
                          "value of such that ≡ mod 6 is 4. Let's call M( ) the largest value of " \
                          "< such that ≡ (mod ). So M(6) = 4. Find ∑M( ) for 1 ≤ ≤ 10 ."

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

