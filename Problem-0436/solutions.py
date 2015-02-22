
__problem_title__ = "Unfair wager"
__problem_url___ = "https://projecteuler.net/problem=436"
__problem_description__ = "Julie proposes the following wager to her sister Louise. She suggests " \
                          "they play a game of chance to determine who will wash the dishes. For " \
                          "this game, they shall use a generator of independent random numbers " \
                          "uniformly distributed between 0 and 1. The game starts with = 0. The " \
                          "first player, Louise, adds to different random numbers from the " \
                          "generator until > 1 and records her last random number ' '. The " \
                          "second player, Julie, continues adding to different random numbers " \
                          "from the generator until > 2 and records her last random number ' '. " \
                          "The player with the highest number wins and the loser washes the " \
                          "dishes, i.e. if > the second player wins. For e ample, if the first " \
                          "player draws 0.62 and 0.44, the first player turn ends since " \
                          "0.62+0.44 > 1 and = 0.44. If the second players draws 0.1, 0.27 and " \
                          "0.91, the second player turn ends since 0.62+0.44+0.1+0.27+0.91 > 2 " \
                          "and = 0.91. Since > , the second player wins. Louise thinks about it " \
                          "for a second, and objects: "That's not fair". What is the probability " \
                          "that the second player wins? Give your answer rounded to 10 places " \
                          "behind the decimal point in the form 0.abcdefghij"

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

