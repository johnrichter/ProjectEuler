
__problem_title__ = "Spherical triangles"
__problem_url___ = "https://projecteuler.net/problem=332"
__problem_description__ = "A is a figure formed on the surface of a sphere by three intersecting " \
                          "pairwise in three vertices. Let C( ) be the sphere with the centre " \
                          "(0,0,0) and radius . Let Z( ) be the set of points on the surface of " \
                          "C( ) with integer coordinates. Let T( ) be the set of spherical " \
                          "triangles with vertices in Z( ). Degenerate spherical triangles, " \
                          "formed by three points on the same great arc, are included in T( ). " \
                          "Let A( ) be the area of the smallest spherical triangle in T( ). For " \
                          "example A(14) is 3.294040 rounded to six decimal places. Find A( ). " \
                          "Give your answer rounded to six decimal places."

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

