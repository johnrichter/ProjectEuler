
__problem_title__ = "Super Ramvok"
__problem_url___ = "https://projecteuler.net/problem=470"
__problem_description__ = "Consider a single game of Ramvok: Let represent the maximum number of " \
                          "turns the game lasts. If = 0, then the game ends immediately. " \
                          "Otherwise, on each turn , the player rolls a die. After rolling, if < " \
                          "the player can either stop the game and receive a prize equal to the " \
                          "value of the current roll, or discard the roll and try again next " \
                          "turn. If = , then the roll cannot be discarded and the prize must be " \
                          "accepted. Before the game begins, is chosen by the player, who must " \
                          "then pay an up-front cost for some constant . For = 0, can be chosen " \
                          "to be infinite (with an up-front cost of 0). Let R( , ) be the " \
                          "expected profit (i.e. net gain) that the player receives from a " \
                          "single game of optimally-played Ramvok, given a fair -sided die and " \
                          "cost constant . For example, R(4, 0.2) = 2.65. Assume that the player " \
                          "has sufficient funds for paying any/all up-front costs. Now consider " \
                          "a game of Super Ramvok: In Super Ramvok, the game of Ramvok is played " \
                          "repeatedly, but with a slight modification. After each game, the die " \
                          "is altered. The alteration process is as follows: The die is rolled " \
                          "once, and if the resulting face has its pips visible, then that face " \
                          "is altered to be blank instead. If the face is already blank, then it " \
                          "is changed back to its original value. After the alteration is made, " \
                          "another game of Ramvok can begin (and during such a game, at each " \
                          "turn, the die is rolled until a face with a value on it appears). The " \
                          "player knows which faces are blank and which are not at all times. " \
                          "The game of Super Ramvok ends once all faces of the die are blank. " \
                          "Let S( , ) be the expected profit that the player receives from an " \
                          "optimally-played game of Super Ramvok, given a fair -sided die to " \
                          "start (with all sides visible), and cost constant . For example, S(6, " \
                          "1) = 208.3. Let F( ) = ∑ ∑ S( , ). Calculate F(20), rounded to the " \
                          "nearest integer."

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

