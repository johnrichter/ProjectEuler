
__problem_title__ = "Consecutive positive divisors"
__problem_url___ = "https://projecteuler.net/problem=179"
__problem_description__ = "Find the number of integers 1 < n < 10 , for which and + 1 have the " \
                          "same number of positive divisors. For example, 14 has the positive " \
                          "divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15."

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

