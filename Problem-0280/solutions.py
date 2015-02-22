
__problem_title__ = "Ant and seeds"
__problem_url___ = "https://projecteuler.net/problem=280"
__problem_description__ = "A laborious ant walks randomly on a 5x5 grid. The walk starts from " \
                          "the central square. At each step, the ant moves to an adjacent square " \
                          "at random, without leaving the grid; thus there are 2, 3 or 4 " \
                          "possible moves at each step depending on the ant's position. At the " \
                          "start of the walk, a seed is placed on each square of the lower row. " \
                          "When the ant isn't carrying a seed and reaches a square of the lower " \
                          "row containing a seed, it will start to carry the seed. The ant will " \
                          "drop the seed on the first empty square of the upper row it " \
                          "eventually reaches. What's the expected number of steps until all " \
                          "seeds have been dropped in the top row? Give your answer rounded to 6 " \
                          "decimal places."

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

