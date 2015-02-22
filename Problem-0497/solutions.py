
__problem_title__ = "Drunken Tower of Hanoi"
__problem_url___ = "https://projecteuler.net/problem=497"
__problem_description__ = "Bob is very familiar with the famous mathematical puzzle/game, "Tower " \
                          "of Hanoi," which consists of three upright rods and disks of " \
                          "different sizes that can slide onto any of the rods. The game begins " \
                          "with a stack of disks placed on the leftmost rod in descending order " \
                          "by size. The objective of the game is to move all of the disks from " \
                          "the leftmost rod to the rightmost rod, given the following " \
                          "restrictions: Moving on to a variant of this game, consider a long " \
                          "room units (square tiles) wide, labeled from 1 to in ascending order. " \
                          "Three rods are placed at squares , , and , and a stack of disks is " \
                          "placed on the rod at square . Bob begins the game standing at square " \
                          ". His objective is to play the Tower of Hanoi game by moving all of " \
                          "the disks to the rod at square . However, Bob can only pick up or set " \
                          "down a disk if he is on the same square as the rod / stack in " \
                          "question. Unfortunately, Bob is also drunk. On a given move, Bob will " \
                          "either stumble one square to the left or one square to the right with " \
                          "equal probability, unless Bob is at either end of the room, in which " \
                          "case he can only move in one direction. Despite Bob's inebriated " \
                          "state, he is still capable of following the rules of the game itself, " \
                          "as well as choosing when to pick up or put down a disk. The following " \
                          "animation depicts a side-view of a sample game for = 3, = 7, = 2, = " \
                          "4, and = 6: Let E( , , , , ) be the expected number of squares that " \
                          "Bob travels during a single optimally-played game. A game is played " \
                          "optimally if the number of disk-pickups is minimized. Interestingly " \
                          "enough, the result is always an integer. For example, E(2,5,1,3,5) = " \
                          "60 and E(3,20,4,9,17) = 2358. Find the last nine digits of ∑ E( ,10 " \
                          ",3 ,6 ,9 )."

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

