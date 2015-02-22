
__problem_title__ = "Number Sequence Game"
__problem_url___ = "https://projecteuler.net/problem=477"
__problem_description__ = "The number sequence game starts with a sequence of numbers written on " \
                          "a line. Two players alternate turns. At his turn, a player must " \
                          "select and remove either the first or the last number remaining in " \
                          "the sequence. The player score is the sum of all the numbers he has " \
                          "taken. Each player attempts to maximize his own sum. Player 1 score " \
                          "is 1 + 10 = 11. Let ( ) be the score of player 1 if both players " \
                          "follow the optimal strategy for the sequence = { , , ..., } defined " \
                          "as: The sequence begins with = {0, 45, 2070, 4284945, 753524550, " \
                          "478107844, 894218625, ...}. You are given (2) = 45, (4) = 4284990, " \
                          "(100) = 26365463243, (10 ) = 2495838522951. Find (10 )."

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

