
__problem_title__ = "Integer Ladders"
__problem_url___ = "https://projecteuler.net/problem=309"
__problem_description__ = "In the classic "Crossing Ladders" problem, we are given the lengths " \
                          "and of two ladders resting on the opposite walls of a narrow, level " \
                          "street. We are also given the height above the street where the two " \
                          "ladders cross and we are asked to find the width of the street ( ). " \
                          "Here, we are only concerned with instances where all four variables " \
                          "are positive integers. For example, if = 70, = 119 and = 30, we can " \
                          "calculate that = 56. In fact, for integer values , , and 0 x y x, , ) " \
                          "producing integer solutions for : (70, 119, 30), (74, 182, 21), (87, " \
                          "105, 35), (100, 116, 35) and (119, 175, 40). For integer values , , " \
                          "and 0 x y x, , ) produce integer solutions for ?"

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

