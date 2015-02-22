
__problem_title__ = "Triangles with integral sides and an integral angle "
__problem_url___ = "https://projecteuler.net/problem=279"
__problem_description__ = "How many triangles are there with integral sides, at least one " \
                          "integral angle (measured in degrees), and a perimeter that does not " \
                          "exceed 10 ?"

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

