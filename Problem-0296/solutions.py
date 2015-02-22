
__problem_title__ = "Angular Bisector and Tangent"
__problem_url___ = "https://projecteuler.net/problem=296"
__problem_description__ = "Given is an integer sided triangle with ≤ ≤ . is the angular bisector " \
                          "of angle . is the tangent at to the circumscribed circle of . is a " \
                          "line parallel to through . The intersection of and is called . How " \
                          "many triangles with a perimeter not exceeding 100 000 exist such that " \
                          "has integral length?"

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

