
__problem_title__ = "Laserbeam"
__problem_url___ = "https://projecteuler.net/problem=202"
__problem_description__ = "Three mirrors are arranged in the shape of an equilateral triangle, " \
                          "with their reflective surfaces pointing inwards. There is an " \
                          "infinitesimal gap at each vertex of the triangle through which a " \
                          "laser beam may pass. Label the vertices A, B and C. There are 2 ways " \
                          "in which a laser beam may enter vertex C, bounce off 11 surfaces, " \
                          "then exit through the same vertex: one way is shown below; the other " \
                          "is the reverse of that. There are 80840 ways in which a laser beam " \
                          "may enter vertex C, bounce off 1000001 surfaces, then exit through " \
                          "the same vertex. In how many ways can a laser beam enter at vertex C, " \
                          "bounce off 12017639147 surfaces, then exit through the same vertex?"

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

