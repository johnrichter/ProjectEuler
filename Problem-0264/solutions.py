
__problem_title__ = "Triangle Centres"
__problem_url___ = "https://projecteuler.net/problem=264"
__problem_description__ = "Consider all the triangles having: There are nine such triangles " \
                          "having a perimeter ≤ 50. Listed and shown in ascending order of their " \
                          "perimeter, they are: The sum of their perimeters, rounded to four " \
                          "decimal places, is 291.0089. Find all such triangles with a perimeter " \
                          "≤ 10 . Enter as your answer the sum of their perimeters rounded to " \
                          "four decimal places."

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

