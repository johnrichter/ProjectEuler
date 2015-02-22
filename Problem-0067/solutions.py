
__problem_title__ = "Maximum path sum II"
__problem_url___ = "https://projecteuler.net/problem=67"
__problem_description__ = "By starting at the top of the triangle below and moving to adjacent " \
                          "numbers on the row below, the maximum total from top to bottom is 23. " \
                          "4 2 6 8 5 3 That is, 3 + 7 + 4 + 9 = 23. Find the maximum total from " \
                          "top to bottom in (right click and 'Save Link/Target As...'), a 15K " \
                          "text file containing a triangle with one-hundred rows. This is a much " \
                          "more difficult version of . It is not possible to try every route to " \
                          "solve this problem, as there are 2 altogether! If you could check one " \
                          "trillion (10 ) routes every second it would take over twenty billion " \
                          "years to check them all. There is an efficient algorithm to solve it. " \
                          ";o)"

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

