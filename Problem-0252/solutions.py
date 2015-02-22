
__problem_title__ = "Convex Holes"
__problem_url___ = "https://projecteuler.net/problem=252"
__problem_description__ = "Given a set of points on a plane, we define a convex hole to be a " \
                          "convex polygon having as vertices any of the given points and not " \
                          "containing any of the given points in its interior (in addition to " \
                          "the vertices, other given points may lie on the perimeter of the " \
                          "polygon). As an example, the image below shows a set of twenty points " \
                          "and a few such convex holes. The convex hole shown as a red heptagon " \
                          "has an area equal to 1049694.5 square units, which is the highest " \
                          "possible area for a convex hole on the given set of points. For our " \
                          "example, we used the first 20 points ( , ), for = 1,2,…,20, produced " \
                          "with the pseudo-random number generator: (527, 144), (−488, 732), " \
                          "(−454, −947), … What is the maximum area for a convex hole on the set " \
                          "containing the first 500 points in the pseudo-random sequence? " \
                          "Specify your answer including one digit after the decimal point."

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

