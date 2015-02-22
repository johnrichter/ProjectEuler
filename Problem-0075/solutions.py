
__problem_title__ = "Singular integer right triangles"
__problem_url___ = "https://projecteuler.net/problem=75"
__problem_description__ = "It turns out that 12 cm is the smallest length of wire that can be " \
                          "bent to form an integer sided right angle triangle in exactly one " \
                          "way, but there are many more examples. : (3,4,5) : (6,8,10) : " \
                          "(5,12,13) : (9,12,15) : (8,15,17) : (12,16,20) In contrast, some " \
                          "lengths of wire, like 20 cm, cannot be bent to form an integer sided " \
                          "right angle triangle, and other lengths allow more than one solution " \
                          "to be found; for example, using 120 cm it is possible to form exactly " \
                          "three different integer sided right angle triangles. : (30,40,50), " \
                          "(20,48,52), (24,45,51) Given that L is the length of the wire, for " \
                          "how many values of L ≤ 1,500,000 can exactly one integer sided right " \
                          "angle triangle be formed?"

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

