
__problem_title__ = "Triangles containing the origin"
__problem_url___ = "https://projecteuler.net/problem=184"
__problem_description__ = "Consider the set of points ( , ) with integer co-ordinates in the " \
                          "interior of the circle with radius , centered at the origin, i.e. + < " \
                          ". For a radius of 2, contains the nine points (0,0), (1,0), (1,1), " \
                          "(0,1), (-1,1), (-1,0), (-1,-1), (0,-1) and (1,-1). There are eight " \
                          "triangles having all three vertices in which contain the origin in " \
                          "the interior. Two of them are shown below, the others are obtained " \
                          "from these by rotation. For a radius of 3, there are 360 triangles " \
                          "containing the origin in the interior and having all vertices in and " \
                          "for the number is 10600. How many triangles are there containing the " \
                          "origin in the interior and having all three vertices in ?"

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

