
__problem_title__ = "Three similar triangles"
__problem_url___ = "https://projecteuler.net/problem=299"
__problem_description__ = "Four points with integer coordinates are selected: A( , 0), B( , 0), " \
                          "C(0, ) and D(0, ), with 0 < < and 0 < < . Point P, also with integer " \
                          "coordinates, is chosen on the line AC so that the three triangles " \
                          "ABP, CDP and BDP are all . It is easy to prove that the three " \
                          "triangles can be similar, only if = . So, given that = , we are " \
                          "looking for triplets ( , , ) such that at least one point P (with " \
                          "integer coordinates) exists on AC, making the three triangles ABP, " \
                          "CDP and BDP all similar. For example, if ( , , )=(2,3,4), it can be " \
                          "easily verified that point P(1,1) satisfies the above condition. Note " \
                          "that the triplets (2,3,4) and (2,4,3) are considered as distinct, " \
                          "although point P(1,1) is common for both. If + < 100, there are 92 " \
                          "distinct triplets ( , , ) such that point P exists. If + < 100 000, " \
                          "there are 320471 distinct triplets ( , , ) such that point P exists. " \
                          "If + < 100 000 000, how many distinct triplets ( , , ) are there such " \
                          "that point P exists?"

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

