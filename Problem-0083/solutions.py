
__problem_title__ = "Path sum: four ways"
__problem_url___ = "https://projecteuler.net/problem=83"
__problem_description__ = "NOTE: This problem is a significantly more challenging version of . " \
                          "In the 5 by 5 matrix below, the minimal path sum from the top left to " \
                          "the bottom right, by moving left, right, up, and down, is indicated " \
                          "in bold red and is equal to 2297. Find the minimal path sum, in " \
                          "(right click and "Save Link/Target As..."), a 31K text file " \
                          "containing a 80 by 80 matrix, from the top left to the bottom right " \
                          "by moving left, right, up, and down."

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

