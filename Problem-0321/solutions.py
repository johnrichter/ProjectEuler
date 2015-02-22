
__problem_title__ = "Swapping Counters"
__problem_url___ = "https://projecteuler.net/problem=321"
__problem_description__ = "A horizontal row comprising of 2 + 1 squares has red counters placed " \
                          "at one end and blue counters at the other end, being separated by a " \
                          "single empty square in the centre. For example, when = 3. A counter " \
                          "can move from one square to the next (slide) or can jump over another " \
                          "counter (hop) as long as the square next to that counter is " \
                          "unoccupied. Let M( ) represent the minimum number of moves/actions to " \
                          "completely reverse the positions of the coloured counters; that is, " \
                          "move all the red counters to the right and all the blue counters to " \
                          "the left. It can be verified M(3) = 15, which also happens to be a " \
                          "triangle number. If we create a sequence based on the values of for " \
                          "which M( ) is a triangle number then the first five terms would be: " \
                          "1, 3, 10, 22, and 63, and their sum would be 99. Find the sum of the " \
                          "first forty terms of this sequence."

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

