
__problem_title__ = "Totient sum"
__problem_url___ = "https://projecteuler.net/problem=432"
__problem_description__ = "Let S( ) = ∑φ( ) for 1 ≤ . (φ is Euler's totient function) You are " \
                          "given that S(510510,10 )= 45480596821125120. Find S(510510,10 ). Give " \
                          "the last 9 digits of your answer."

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

