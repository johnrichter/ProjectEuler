
__problem_title__ = "Scary Sphere"
__problem_url___ = "https://projecteuler.net/problem=360"
__problem_description__ = "Given two points (x ,y ,z ) and (x ,y ,z ) in three dimensional " \
                          "space, the between those points is defined as |x -x |+|y -y |+|z -z " \
                          "|. Let C( ) be a sphere with radius and center in the origin " \
                          "O(0,0,0). Let I( ) be the set of all points with integer coordinates " \
                          "on the surface of C( ). Let S( ) be the sum of the Manhattan " \
                          "distances of all elements of I( ) to the origin O. E.g. S(45)=34518. " \
                          "Find S(10 )."

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

