
__problem_title__ = "Integer sided triangles for which the  area/perimeter ratio is integral"
__problem_url___ = "https://projecteuler.net/problem=283"
__problem_description__ = "Consider the triangle with sides 6, 8 and 10. It can be seen that the " \
                          "perimeter and the area are both equal to 24. So the area/perimeter " \
                          "ratio is equal to 1. Consider also the triangle with sides 13, 14 and " \
                          "15. The perimeter equals 42 while the area is equal to 84. So for " \
                          "this triangle the area/perimeter ratio is equal to 2. Find the sum of " \
                          "the perimeters of all integer sided triangles for which the " \
                          "area/perimeter ratios are equal to positive integers not exceeding " \
                          "1000."

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

