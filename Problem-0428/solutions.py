
__problem_title__ = "Necklace of circles"
__problem_url___ = "https://projecteuler.net/problem=428"
__problem_description__ = "Let , and be positive numbers. Let W, X, Y, Z be four collinear " \
                          "points where |WX| = , |XY| = , |YZ| = and |WZ| = + + . Let C be the " \
                          "circle having the diameter XY. Let C be the circle having the " \
                          "diameter WZ. The triplet ( , , ) is called a if you can place ≥ 3 " \
                          "distinct circles C , C , ..., C such that: For example, (5, 5, 5) and " \
                          "(4, 3, 21) are necklace triplets, while it can be shown that (2, 2, " \
                          "5) is not. Let T( ) be the number of necklace triplets ( , , ) such " \
                          "that , and are positive integers, and ≤ . For example, T(1) = 9, " \
                          "T(20) = 732 and T(3000) = 438106. Find T(1 000 000 000)."

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

