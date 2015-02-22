
__problem_title__ = "Perfect Square Collection"
__problem_url___ = "https://projecteuler.net/problem=142"
__problem_description__ = "Find the smallest x + y + z with integers x > y > z > 0 such that x + " \
                          "y, x − y, x + z, x − z, y + z, y − z are all perfect squares."

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

