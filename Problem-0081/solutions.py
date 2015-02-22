
__problem_title__ = "Path sum: two ways"
__problem_url___ = "https://projecteuler.net/problem=81"
__problem_description__ = "In the 5 by 5 matrix below, the minimal path sum from the top left to " \
                          "the bottom right, by , is indicated in bold red and is equal to 2427. " \
                          "Find the minimal path sum, in (right click and "Save Link/Target " \
                          "As..."), a 31K text file containing a 80 by 80 matrix, from the top " \
                          "left to the bottom right by only moving right and down."

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

