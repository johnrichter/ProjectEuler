
__problem_title__ = "Hopping Game"
__problem_url___ = "https://projecteuler.net/problem=391"
__problem_description__ = "Let be the number of 1’s when writing the numbers from 0 to in " \
                          "binary. For example, writing 0 to 5 in binary, we have 0, 1, 10, 11, " \
                          "100, 101. There are seven 1’s, so = 7. The sequence S = { : ≥ 0} " \
                          "starts {0, 1, 2, 4, 5, 7, 9, 12, ...}. A game is played by two " \
                          "players. Before the game starts, a number is chosen. A counter starts " \
                          "at 0. At each turn, the player chooses a number from 1 to (inclusive) " \
                          "and increases by that number. The resulting value of must be a member " \
                          "of S. If there are no more valid moves, the player loses. For " \
                          "example: Let = 5. starts at 0. Player 1 chooses 4, so becomes 0 + 4 = " \
                          "4. Player 2 chooses 5, so becomes 4 + 5 = 9. Player 1 chooses 3, so " \
                          "becomes 9 + 3 = 12. etc. Note that must always belong to S, and each " \
                          "player can increase by at most . Let M( ) be the highest number the " \
                          "first player can choose at her first turn to force a win, and M( ) = " \
                          "0 if there is no such move. For example, M(2) = 2, M(7) = 1 and M(20) " \
                          "= 4. Given Σ(M( )) = 8150 for 1 ≤ ≤ 20. Find Σ(M( )) for 1 ≤ ≤ 1000."

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

