
__problem_title__ = "Building a tower"
__problem_url___ = "https://projecteuler.net/problem=324"
__problem_description__ = "Let ( ) represent the number of ways one can fill a 3×3× tower with " \
                          "blocks of 2×1×1. You're allowed to rotate the blocks in any way you " \
                          "like; however, rotations, reflections etc of the tower itself are " \
                          "counted as distinct. For example (with = 100000007) : (2) = 229, (4) " \
                          "= 117805, (10) mod = 96149360, (10 ) mod = 24806056, (10 ) mod = " \
                          "30808124. Find (10 ) mod 100000007."

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

