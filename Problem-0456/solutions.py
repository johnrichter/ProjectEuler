
__problem_title__ = "Triangles containing the origin II"
__problem_url___ = "https://projecteuler.net/problem=456"
__problem_description__ = "Define: = (1248 mod 32323) - 16161 = (8421 mod 30103) - 15051 P = {( " \
                          ", ), ( , ), ..., ( , )} For example, P = {(-14913, -6630), (-10161, " \
                          "5625), (5226, 11896), (8340, -10778), (15852, -5203), (-15165, " \
                          "11295), (-1427, -14495), (12407, 1060)}. Let C( ) be the number of " \
                          "triangles whose vertices are in P which contain the origin in the " \
                          "interior. Examples: C(8) = 20 C(600) = 8950634 C(40 000) = " \
                          "2666610948988 Find C(2 000 000)."

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

