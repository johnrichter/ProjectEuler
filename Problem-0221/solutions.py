
__problem_title__ = "Alexandrian Integers"
__problem_url___ = "https://projecteuler.net/problem=221"
__problem_description__ = "We shall call a positive integer an "Alexandrian integer", if there " \
                          "exist integers , , such that: For example, 630 is an Alexandrian " \
                          "integer ( = 5, = −7, = −18). In fact, 630 is the 6 Alexandrian " \
                          "integer, the first 6 Alexandrian integers being: 6, 42, 120, 156, 420 " \
                          "and 630. Find the 150000 Alexandrian integer."

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

