
__problem_title__ = "Eulerian Cycles"
__problem_url___ = "https://projecteuler.net/problem=289"
__problem_description__ = "Let C( , ) be a circle passing through the points ( , ), ( , +1), ( " \
                          "+1, ) and ( +1, +1). For positive integers m and n, let E( , ) be a " \
                          "configuration which consists of the · circles: { C( , ): 0 ≤ m, 0 ≤ " \
                          "n, and are integers } An Eulerian cycle on E( , ) is a closed path " \
                          "that passes through each arc exactly once. Many such paths are " \
                          "possible on E( , ), but we are only interested in those which are not " \
                          "self-crossing: A non-crossing path just touches itself at lattice " \
                          "points, but it never crosses itself. The image below shows E(3,3) and " \
                          "an example of an Eulerian non-crossing path. Let L( , ) be the number " \
                          "of Eulerian non-crossing paths on E( , ). For example, L(1,2) = 2, " \
                          "L(2,2) = 37 and L(3,3) = 104290. Find L(6,10) mod 10 ."

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

