
__problem_title__ = "Counting Sundays"
__problem_url___ = "https://projecteuler.net/problem=19"
__problem_description__ = "You are given the following information, but you may prefer to do " \
                          "some research for yourself. How many Sundays fell on the first of the " \
                          "month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"

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

