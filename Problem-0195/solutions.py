
__problem_title__ = "Inscribed circles of triangles with one angle of 60 degrees"
__problem_url___ = "https://projecteuler.net/problem=195"
__problem_description__ = "Let's call an integer sided triangle with exactly one angle of 60 " \
                          "degrees a 60-degree triangle. Let be the radius of the inscribed " \
                          "circle of such a 60-degree triangle. There are 1234 60-degree " \
                          "triangles for which ≤ 100. Let T( ) be the number of 60-degree " \
                          "triangles for which ≤ , so T(100) = 1234, T(1000) = 22767, and " \
                          "T(10000) = 359912. Find T(1053779)."

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

