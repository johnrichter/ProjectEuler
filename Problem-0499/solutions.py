
__problem_title__ = "St. Petersburg Lottery"
__problem_url___ = "https://projecteuler.net/problem=499"
__problem_description__ = "A gambler decides to participate in a special lottery. In this " \
                          "lottery the gambler plays a series of one or more games. Each game " \
                          "costs pounds to play and starts with an initial pot of 1 pound. The " \
                          "gambler flips an unbiased coin. Every time a head appears, the pot is " \
                          "doubled and the gambler continues. When a tail appears, the game ends " \
                          "and the gambler collects the current value of the pot. The gambler is " \
                          "certain to win at least 1 pound, the starting value of the pot, at " \
                          "the cost of pounds, the initial fee. The gambler cannot continue to " \
                          "play if his fortune falls below pounds. Let ( ) denote the " \
                          "probability that the gambler will never run out of money in this " \
                          "lottery given his initial fortune and the cost per game . For example " \
                          "(2) ≈ 0.2522, (5) ≈ 0.6873 and (10 000) ≈ 0.9952 (note: ( ) = 0 for " \
                          "m). Find (10 ) and give your answer rounded to 7 decimal places " \
                          "behind the decimal point in the form 0.abcdefg."

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

