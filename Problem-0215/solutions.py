
__problem_title__ = "Crack-free Walls"
__problem_url___ = "https://projecteuler.net/problem=215"
__problem_description__ = "Consider the problem of building a wall out of 2×1 and 3×1 bricks " \
                          "(horizontal×vertical dimensions) such that, for extra strength, the " \
                          "gaps between horizontally-adjacent bricks never line up in " \
                          "consecutive layers, i.e. never form a "running crack". For example, " \
                          "the following 9×3 wall is not acceptable due to the running crack " \
                          "shown in red: There are eight ways of forming a crack-free 9×3 wall, " \
                          "written W(9,3) = 8. Calculate W(32,10)."

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

