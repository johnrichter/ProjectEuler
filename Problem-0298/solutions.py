
__problem_title__ = "Selective Amnesia"
__problem_url___ = "https://projecteuler.net/problem=298"
__problem_description__ = "Larry and Robin play a memory game involving of a sequence of random " \
                          "numbers between 1 and 10, inclusive, that are called out one at a " \
                          "time. Each player can remember up to 5 previous numbers. When the " \
                          "called number is in a player's memory, that player is awarded a " \
                          "point. If it's not, the player adds the called number to his memory, " \
                          "removing another number if his memory is full. Both players start " \
                          "with empty memories. Both players always add new missed numbers to " \
                          "their memory but use a different strategy in deciding which number to " \
                          "remove: Larry's strategy is to remove the number that hasn't been " \
                          "called in the longest time. Robin's strategy is to remove the number " \
                          "that's been in the memory the longest time. Example game: Denoting " \
                          "Larry's score by and Robin's score by , what is the expected value of " \
                          "| - | after 50 turns? Give your answer rounded to eight decimal " \
                          "places using the format x.xxxxxxxx ."

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

