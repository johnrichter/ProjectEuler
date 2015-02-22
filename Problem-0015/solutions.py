
__problem_title__ = "Lattice paths"
__problem_url___ = "https://projecteuler.net/problem=15"
__problem_description__ = "Starting in the top left corner of a 2×2 grid, and only being able to " \
                          "move to the right and down, there are exactly 6 routes to the bottom " \
                          "right corner. How many such routes are there through a 20×20 grid?"

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

