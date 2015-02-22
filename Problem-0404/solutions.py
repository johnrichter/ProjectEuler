
__problem_title__ = "Crisscross Ellipses"
__problem_url___ = "https://projecteuler.net/problem=404"
__problem_description__ = "E is an ellipse with an equation of the form x + 4y = 4 . E ' is the " \
                          "rotated image of E by θ degrees counterclockwise around the origin " \
                          "O(0, 0) for 0° < θ < 90°. is the distance to the origin of the two " \
                          "intersection points closest to the origin and is the distance of the " \
                          "two other intersection points. We call an ordered triplet ( , , ) a " \
                          "if , and are positive integers. For example, (209, 247, 286) is a " \
                          "canonical ellipsoidal triplet. Let C( ) be the number of distinct " \
                          "canonical ellipsoidal triplets ( , , ) for ≤ . It can be verified " \
                          "that C(10 ) = 7, C(10 ) = 106 and C(10 ) = 11845. Find C(10 )."

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

