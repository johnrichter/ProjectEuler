
__problem_title__ = "A Scoop of Blancmange"
__problem_url___ = "https://projecteuler.net/problem=226"
__problem_description__ = "The is the set of points ( , ) such that 0 ≤ ≤ 1 and , where ( ) = " \
                          "the distance from to the nearest integer. The area under the " \
                          "blancmange curve is equal to ½, shown in pink in the diagram below. " \
                          "Let be the circle with centre (¼,&frac12) and radius ¼, shown in " \
                          "black in the diagram. What area under the blancmange curve is " \
                          "enclosed by ? Give your answer rounded to eight decimal places in the " \
                          "form"

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

