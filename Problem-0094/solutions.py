
__problem_title__ = "Almost equilateral triangles"
__problem_url___ = "https://projecteuler.net/problem=94"
__problem_description__ = "It is easily proved that no equilateral triangle exists with integral " \
                          "length sides and integral area. However, the 5-5-6 has an area of 12 " \
                          "square units. We shall define an to be a triangle for which two sides " \
                          "are equal and the third differs by no more than one unit. Find the " \
                          "sum of the perimeters of all with integral side lengths and area and " \
                          "whose perimeters do not exceed one billion (1,000,000,000)."

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

