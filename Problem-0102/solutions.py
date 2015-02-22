
__problem_title__ = "Triangle containment"
__problem_url___ = "https://projecteuler.net/problem=102"
__problem_description__ = "Three distinct points are plotted at random on a Cartesian plane, for " \
                          "which -1000 ≤ , ≤ 1000, such that a triangle is formed. Consider the " \
                          "following two triangles: A(-340,495), B(-153,-910), C(835,-947) " \
                          "X(-175,41), Y(-421,-714), Z(574,-645) It can be verified that " \
                          "triangle ABC contains the origin, whereas triangle XYZ does not. " \
                          "Using (right click and 'Save Link/Target As...'), a 27K text file " \
                          "containing the co-ordinates of one thousand "random" triangles, find " \
                          "the number of triangles for which the interior contains the origin. " \
                          "NOTE: The first two examples in the file represent the triangles in " \
                          "the example given above."

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

