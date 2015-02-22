
__problem_title__ = "Incenter and circumcenter of triangle"
__problem_url___ = "https://projecteuler.net/problem=496"
__problem_description__ = "Given an integer sided triangle ABC: Let I be the incenter of ABC. " \
                          "Let D be the intersection between the line AI and the circumcircle of " \
                          "ABC (A ≠ D). We define F( ) as the sum of BC for the triangles ABC " \
                          "that satisfy AC = DI and BC ≤ . For example, F(15) = 45 because the " \
                          "triangles ABC with (BC,AC,AB) = (6,4,5), (12,8,10), (12,9,7), " \
                          "(15,9,16) satisfy the conditions. Find F(10 )."

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

