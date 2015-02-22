
__problem_title__ = "Almost right-angled triangles I"
__problem_url___ = "https://projecteuler.net/problem=223"
__problem_description__ = "Let us call an integer sided triangle with sides ≤ ≤ if the sides " \
                          "satisfy + = + 1. How many barely acute triangles are there with " \
                          "perimeter ≤ 25,000,000?"

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

