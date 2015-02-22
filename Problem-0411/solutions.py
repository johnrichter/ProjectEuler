
__problem_title__ = "Uphill paths"
__problem_url___ = "https://projecteuler.net/problem=411"
__problem_description__ = "Let be a positive integer. Suppose there are stations at the " \
                          "coordinates ( , ) = (2 mod , 3 mod ) for 0 ≤ ≤ 2 . We will consider " \
                          "stations with the same coordinates as the same station. We wish to " \
                          "form a path from (0, 0) to ( , ) such that the x and y coordinates " \
                          "never decrease. Let S( ) be the maximum number of stations such a " \
                          "path can pass through. For example, if = 22, there are 11 distinct " \
                          "stations, and a valid path can pass through at most 5 stations. " \
                          "Therefore, S(22) = 5. The case is illustrated below, with an example " \
                          "of an optimal path: It can also be verified that S(123) = 14 and " \
                          "S(10000) = 48. Find ∑ S( ) for 1 ≤ ≤ 30."

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

