
__problem_title__ = "Path sum: three ways"
__problem_url___ = "https://projecteuler.net/problem=82"
__problem_description__ = "NOTE: This problem is a more challenging version of . The minimal " \
                          "path sum in the 5 by 5 matrix below, by starting in any cell in the " \
                          "left column and finishing in any cell in the right column, and only " \
                          "moving up, down, and right, is indicated in red and bold; the sum is " \
                          "equal to 994. Find the minimal path sum, in (right click and "Save " \
                          "Link/Target As..."), a 31K text file containing a 80 by 80 matrix, " \
                          "from the left column to the right column."

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

