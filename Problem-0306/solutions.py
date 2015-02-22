
__problem_title__ = "Paper-strip Game"
__problem_url___ = "https://projecteuler.net/problem=306"
__problem_description__ = "The following game is a classic example of Combinatorial Game Theory: " \
                          "Two players start with a strip of white squares and they take " \
                          "alternate turns. On each turn, a player picks two contiguous white " \
                          "squares and paints them black. The first player who cannot make a " \
                          "move loses. So, for 1 ≤ ≤ 5, there are 3 values of for which the " \
                          "first player can force a win. Similarly, for 1 ≤ ≤ 50, there are 40 " \
                          "values of for which the first player can force a win. For 1 ≤ ≤ 1 000 " \
                          "000, how many values of are there for which the first player can " \
                          "force a win?"

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

