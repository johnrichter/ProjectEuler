
__problem_title__ = "BÃ©zier Curves"
__problem_url___ = "https://projecteuler.net/problem=363"
__problem_description__ = "A cubic Bézier curve is defined by four points: P , P , P and P . The " \
                          "curve is constructed as follows: On the segments P P , P P and P P " \
                          "the points Q ,Q and Q are drawn such that P Q / P P = P Q / P P = P Q " \
                          "/ P P = t (t in [0,1]). On the segments Q Q and Q Q the points R and " \
                          "R are drawn such that Q R / Q Q = Q R / Q Q = t for the same value of " \
                          "t. On the segment R R the point B is drawn such that R B / R R = t " \
                          "for the same value of t. The Bézier curve defined by the points P , P " \
                          ", P , P is the locus of B as Q takes all possible positions on the " \
                          "segment P P . (Please note that for all points the value of t is the " \
                          "same.) At you will find an applet that allows you to drag the points " \
                          "P , P , P and P to see what the Bézier curve (green curve) defined by " \
                          "those points looks like. You can also drag the point Q along the " \
                          "segment P P . From the construction it is clear that the Bézier curve " \
                          "will be tangent to the segments P P in P and P P in P . A cubic " \
                          "Bézier curve with P =(1,0), P =(1, ), P =( ,1) and P =(0,1) is used " \
                          "to approximate a quarter circle. The value > 0 is chosen such that " \
                          "the area enclosed by the lines OP , OP and the curve is equal to / " \
                          "(the area of the quarter circle)."

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

