
__problem_title__ = "Self powers"
__problem_url___ = "https://projecteuler.net/problem=48"
__problem_description__ = "The series, 1 + 2 + 3 + ... + 10 = 10405071317. Find the last ten " \
                          "digits of the series, 1 + 2 + 3 + ... + 1000 ."

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

