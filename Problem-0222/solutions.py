
__problem_title__ = "Sphere Packing"
__problem_url___ = "https://projecteuler.net/problem=222"
__problem_description__ = "What is the length of the shortest pipe, of internal radius 50mm, " \
                          "that can fully contain 21 balls of radii 30mm, 31mm, ..., 50mm? Give " \
                          "your answer in micrometres (10 m) rounded to the nearest integer."

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

