
__problem_title__ = "Sum of sum of divisors"
__problem_url___ = "https://projecteuler.net/problem=439"
__problem_description__ = "Let ( ) be the sum of all divisors of . We define the function S( ) = " \
                          "∑ ∑ ( · ). For example, S(3) = (1) + (2) + (3) + (2) + (4) + (6) + " \
                          "(3) + (6) + (9) = 59. You are given that S(10 ) = 563576517282 and " \
                          "S(10 ) mod 10 = 215766508. Find S(10 ) mod 10 ."

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

