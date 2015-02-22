
__problem_title__ = "Cutting rope"
__problem_url___ = "https://projecteuler.net/problem=398"
__problem_description__ = "Inside a rope of length , -1 points are placed with distance 1 from " \
                          "each other and from the endpoints. Among these points, we choose -1 " \
                          "points at random and cut the rope at these points to create segments. " \
                          "Let E( , ) be the expected length of the second-shortest segment. For " \
                          "example, E(3, 2) = 2 and E(8, 3) = 16/7. Note that if multiple " \
                          "segments have the same shortest length the length of the " \
                          "second-shortest segment is defined as the same as the shortest " \
                          "length. Find E(10 , 100). Give your answer rounded to 5 decimal " \
                          "places behind the decimal point."

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

