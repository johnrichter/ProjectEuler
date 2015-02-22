
__problem_title__ = "Robot Walks"
__problem_url___ = "https://projecteuler.net/problem=208"
__problem_description__ = "A robot moves in a series of one-fifth circular arcs (72°), with a " \
                          "free choice of a clockwise or an anticlockwise arc for each step, but " \
                          "no turning on the spot. One of 70932 possible closed paths of 25 arcs " \
                          "starting northward is Given that the robot starts facing North, how " \
                          "many journeys of 70 arcs in length can it take that return it, after " \
                          "the final arc, to its starting position? (Any arc may be traversed " \
                          "multiple times.)"

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

