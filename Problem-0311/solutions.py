
__problem_title__ = "Biclinic Integral Quadrilaterals"
__problem_url___ = "https://projecteuler.net/problem=311"
__problem_description__ = "ABCD is a convex, integer sided quadrilateral with 1 ≤ AB < BC < CD < " \
                          "AD. BD has integer length. O is the midpoint of BD. AO has integer " \
                          "length. We'll call ABCD a if AO = CO ≤ BO = DO. For example, the " \
                          "following quadrilateral is a biclinic integral quadrilateral: AB = " \
                          "19, BC = 29, CD = 37, AD = 43, BD = 48 and AO = CO = 23. Let B( ) be " \
                          "the number of distinct biclinic integral quadrilaterals ABCD that " \
                          "satisfy AB +BC +CD +AD ≤ . We can verify that B(10 000) = 49 and B(1 " \
                          "000 000) = 38239. Find B(10 000 000 000)."

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

