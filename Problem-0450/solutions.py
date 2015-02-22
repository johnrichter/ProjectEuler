
__problem_title__ = "Hypocycloid and Lattice points"
__problem_url___ = "https://projecteuler.net/problem=450"
__problem_description__ = "A hypocycloid is the curve drawn by a point on a small circle rolling " \
                          "inside a larger circle. The parametric equations of a hypocycloid " \
                          "centered at the origin, and starting at the right most point is given " \
                          "by: $x(t) = (R - r) \cos(t) + r \cos(\frac {R - r} r t)$ $y(t) = (R - " \
                          "r) \sin(t) - r \sin(\frac {R - r} r t)$ Where is the radius of the " \
                          "large circle and the radius of the small circle. Let $C(R, r)$ be the " \
                          "set of distinct points with integer coordinates on the hypocycloid " \
                          "with radius and and for which there is a corresponding value of such " \
                          "that $\sin(t)$ and $\cos(t)$ are rational numbers. Let $S(R, r) = " \
                          "\sum_{(x,y) \in C(R, r)} |x| + |y|$ be the sum of the absolute values " \
                          "of the and coordinates of the points in $C(R, r)$. Let $T(N) = " \
                          "\sum_{R = 3}^N \sum_{r=1}^{\lfloor \frac {R - 1} 2 \rfloor} S(R, r)$ " \
                          "be the sum of $S(R, r)$ for and positive integers, $R\leq N$ and $2r " \
                          "You are given: (3, 1) = {(3, 0), (-1, 2), (-1,0), (-1,-2)} (2500, " \
                          "1000) = (3, 1) = (|3| + |0|) + (|-1| + |2|) + (|-1| + |0|) + (|-1| + " \
                          "|-2|) = 10 (3) = 10; (10) = 524 ; (100) = 580442; (10 ) = 583108600. " \
                          "Find (10 )."

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

