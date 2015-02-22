
__problem_title__ = "Combined Volume of Cuboids"
__problem_url___ = "https://projecteuler.net/problem=212"
__problem_description__ = "An , specified by parameters { (x ,y ,z ), (dx,dy,dz) }, consists of " \
                          "all points (X,Y,Z) such that x ≤ X ≤ x +dx, y ≤ Y ≤ y +dy and z ≤ Z ≤ " \
                          "z +dz. The volume of the cuboid is the product, dx × dy × dz. The of " \
                          "a collection of cuboids is the volume of their union and will be less " \
                          "than the sum of the individual volumes if any cuboids overlap. Let C " \
                          ",...,C be a collection of 50000 axis-aligned cuboids such that C has " \
                          "parameters x = S modulo 10000 y = S modulo 10000 z = S modulo 10000 " \
                          "dx = 1 + (S modulo 399) dy = 1 + (S modulo 399) dz = 1 + (S modulo " \
                          "399) where S ,...,S come from the "Lagged Fibonacci Generator": For 1 " \
                          "≤ ≤ 55, S = [100003 - 200003 + 300007 ] (modulo 1000000) For 56 ≤ , S " \
                          "= [S + S ] (modulo 1000000) Thus, C has parameters " \
                          "{(7,53,183),(94,369,56)}, C has parameters " \
                          "{(2383,3563,5079),(42,212,344)}, and so on. The combined volume of " \
                          "the first 100 cuboids, C ,...,C , is 723581599. What is the combined " \
                          "volume of all 50000 cuboids, C ,...,C ?"

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

