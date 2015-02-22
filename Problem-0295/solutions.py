
__problem_title__ = "Lenticular holes"
__problem_url___ = "https://projecteuler.net/problem=295"
__problem_description__ = "We call the convex area enclosed by two circles a if: Consider the " \
                          "circles: C : + =25 C : ( +4) +( -4) =1 C : ( -12) +( -4) =65 The " \
                          "circles C , C and C are drawn in the picture below. C and C form a " \
                          "lenticular hole, as well as C and C . We call an ordered pair of " \
                          "positive real numbers (r , r ) a if there exist two circles with " \
                          "radii r and r that form a lenticular hole. We can verify that (1, 5) " \
                          "and (5, √65) are the lenticular pairs of the example above. Let L(N) " \
                          "be the number of lenticular pairs (r , r ) for which 0 < r ≤ r ≤ N. " \
                          "We can verify that L(10) = 30 and L(100) = 3442. Find L(100 000)."

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

