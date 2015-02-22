
__problem_title__ = "Cuboid route"
__problem_url___ = "https://projecteuler.net/problem=86"
__problem_description__ = "A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by " \
                          "3, and a fly, F, sits in the opposite corner. By travelling on the " \
                          "surfaces of the room the shortest "straight line" distance from S to " \
                          "F is 10 and the path is shown on the diagram. However, there are up " \
                          "to three "shortest" path candidates for any given cuboid and the " \
                          "shortest route doesn't always have integer length. It can be shown " \
                          "that there are exactly 2060 distinct cuboids, ignoring rotations, " \
                          "with integer dimensions, up to a maximum size of M by M by M, for " \
                          "which the shortest route has integer length when M = 100. This is the " \
                          "least value of M for which the number of solutions first exceeds two " \
                          "thousand; the number of solutions when M = 99 is 1975. Find the least " \
                          "value of M such that the number of solutions first exceeds one " \
                          "million."

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

