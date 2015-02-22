
__problem_title__ = "Ellipses inside triangles"
__problem_url___ = "https://projecteuler.net/problem=385"
__problem_description__ = "For any triangle in the plane, it can be shown that there is a unique " \
                          "ellipse with largest area that is completely inside . For a given , " \
                          "consider triangles such that: - the vertices of have integer " \
                          "coordinates with absolute value ≤ n, and - the of the largest-area " \
                          "ellipse inside are (√13,0) and (-√13,0). Let A( ) be the sum of the " \
                          "areas of all such triangles. For example, if = 8, there are two such " \
                          "triangles. Their vertices are (-4,-3),(-4,3),(8,0) and " \
                          "(4,3),(4,-3),(-8,0), and the area of each triangle is 36. Thus A(8) = " \
                          "36 + 36 = 72. It can be verified that A(10) = 252, A(100) = 34632 and " \
                          "A(1000) = 3529008. Find A(1 000 000 000). The (plural of ) of an " \
                          "ellipse are two points A and B such that for every point P on the " \
                          "boundary of the ellipse, + is constant."

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

