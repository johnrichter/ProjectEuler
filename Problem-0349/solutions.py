
__problem_title__ = "Langton's ant"
__problem_url___ = "https://projecteuler.net/problem=349"
__problem_description__ = "An ant moves on a regular grid of squares that are coloured either " \
                          "black or white. The ant is always oriented in one of the cardinal " \
                          "directions (left, right, up or down) and moves from square to " \
                          "adjacent square according to the following rules: - if it is on a " \
                          "black square, it flips the color of the square to white, rotates 90 " \
                          "degrees counterclockwise and moves forward one square. - if it is on " \
                          "a white square, it flips the color of the square to black, rotates 90 " \
                          "degrees clockwise and moves forward one square. Starting with a grid " \
                          "that is entirely white, how many squares are black after 10 moves of " \
                          "the ant?"

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

