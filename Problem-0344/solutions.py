
__problem_title__ = "Silver dollar game"
__problem_url___ = "https://projecteuler.net/problem=344"
__problem_description__ = "One variant of N.G. de Bruijn's game can be described as follows: On " \
                          "a strip of squares a number of coins are placed, at most one coin per " \
                          "square. Only one coin, called the , has any value. Two players take " \
                          "turns making moves. At each turn a player must make either a or a " \
                          "move. A move consists of selecting one coin and moving it one or more " \
                          "squares to the left. The coin cannot move out of the strip or jump on " \
                          "or over another coin. Alternatively, the player can choose to make " \
                          "the move of pocketing the leftmost coin rather than making a regular " \
                          "move. If no regular moves are possible, the player is forced to " \
                          "pocket the leftmost coin. The winner is the player who pockets the " \
                          "silver dollar. A is an arrangement of coins on the strip where the " \
                          "first player can force a win no matter what the second player does. " \
                          "Let W( , ) be the number of winning configurations for a strip of " \
                          "squares, worthless coins and one silver dollar. You are given that " \
                          "W(10,2) = 324 and W(100,10) = 1514704946113500. Find W(1 000 000, " \
                          "100) modulo the semiprime 1000 036 000 099 (= 1 000 003 · 1 000 033)."

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

