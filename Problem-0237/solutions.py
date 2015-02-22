
__problem_title__ = "Tours on a 4 x n playing board"
__problem_url___ = "https://projecteuler.net/problem=237"
__problem_description__ = "Let T( ) be the number of tours over a 4 × playing board such that: " \
                          "The diagram shows one tour over a 4 × 10 board: T(10) is 2329. What " \
                          "is T(10 ) modulo 10 ?"

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

