
__problem_title__ = "Migrating ants"
__problem_url___ = "https://projecteuler.net/problem=393"
__problem_description__ = "An × grid of squares contains ants, one ant per square. All ants " \
                          "decide to move simultaneously to an adjacent square (usually 4 " \
                          "possibilities, except for ants on the edge of the grid or at the " \
                          "corners). We define ( ) to be the number of ways this can happen " \
                          "without any ants ending on the same square and without any two ants " \
                          "crossing the same edge between two squares. You are given that (4) = " \
                          "88. Find (10)."

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

