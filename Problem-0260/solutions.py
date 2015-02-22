
__problem_title__ = "Stone Game"
__problem_url___ = "https://projecteuler.net/problem=260"
__problem_description__ = "A game is played with three piles of stones and two players. At her " \
                          "turn, a player removes one or more stones from the piles. However, if " \
                          "she takes stones from more than one pile, she must remove the same " \
                          "number of stones from each of the selected piles. In other words, the " \
                          "player chooses some N>0 and removes: A is one where the first player " \
                          "can force a win. For example, (0,0,13), (0,11,11) and (5,5,5) are " \
                          "winning configurations because the first player can immediately " \
                          "remove all stones. A is one where the second player can force a win, " \
                          "no matter what the first player does. For example, (0,1,2) and " \
                          "(1,3,3) are losing configurations: any legal move leaves a winning " \
                          "configuration for the second player. Consider all losing " \
                          "configurations (x ,y ,z ) where x ≤ y ≤ z ≤ 100. We can verify that " \
                          "Σ(x +y +z ) = 173895 for these. Find Σ(x +y +z ) where (x ,y ,z ) " \
                          "ranges over the losing configurations with x ≤ y ≤ z ≤ 1000."

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

