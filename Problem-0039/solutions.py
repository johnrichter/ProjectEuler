
__problem_title__ = "Integer right triangles"
__problem_url___ = "https://projecteuler.net/problem=39"
__problem_description__ = "If is the perimeter of a right angle triangle with integral length " \
                          "sides, { , , }, there are exactly three solutions for = 120. " \
                          "{20,48,52}, {24,45,51}, {30,40,50} For which value of ≤ 1000, is the " \
                          "number of solutions maximised?"

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

