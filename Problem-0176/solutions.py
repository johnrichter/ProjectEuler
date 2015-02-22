
__problem_title__ = "Right-angled triangles that share a cathetus"
__problem_url___ = "https://projecteuler.net/problem=176"
__problem_description__ = "The four right-angled triangles with sides (9,12,15), (12,16,20), " \
                          "(5,12,13) and (12,35,37) all have one of the shorter sides (catheti) " \
                          "equal to 12. It can be shown that no other integer sided right-angled " \
                          "triangle exists with one of the catheti equal to 12. Find the " \
                          "smallest integer that can be the length of a cathetus of exactly " \
                          "47547 different integer sided right-angled triangles."

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

