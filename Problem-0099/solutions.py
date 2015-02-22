
__problem_title__ = "Largest exponential"
__problem_url___ = "https://projecteuler.net/problem=99"
__problem_description__ = "Comparing two numbers written in index form like 2 and 3 is not " \
                          "difficult, as any calculator would confirm that 2 = 2048 < 3 = 2187. " \
                          "However, confirming that 632382 > 519432 would be much more " \
                          "difficult, as both numbers contain over three million digits. Using " \
                          "(right click and 'Save Link/Target As...'), a 22K text file " \
                          "containing one thousand lines with a base/exponent pair on each line, " \
                          "determine which line number has the greatest numerical value. NOTE: " \
                          "The first two lines in the file represent the numbers in the example " \
                          "given above."

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

