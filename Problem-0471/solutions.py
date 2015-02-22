
__problem_title__ = "Triangle inscribed in ellipse"
__problem_url___ = "https://projecteuler.net/problem=471"
__problem_description__ = "The triangle ΔABC is inscribed in an ellipse with equation $\frac " \
                          "{x^2} {a^2} + \frac {y^2} {b^2} = 1$, 0 b a, and integers. Let ( , ) " \
                          "be the radius of the incircle of ΔABC when the incircle has center (2 " \
                          ", 0) and A has coordinates $\left( \frac a 2, \frac {\sqrt 3} 2 " \
                          "b\right)$. For example, (3,1) = ½, (6,2) = 1, (12,3) = 2. Let $G(n) = " \
                          "\sum_{a=3}^n \sum_{b=1}^{\lfloor \frac {a - 1} 2 \rfloor} r(a, b)$ " \
                          "You are given (10) = 20.59722222, (100) = 19223.60980 (rounded to 10 " \
                          "significant digits). Find (10 ). Give your answer in scientific " \
                          "notation rounded to 10 significant digits. Use a lowercase e to " \
                          "separate mantissa and exponent. For (10) the answer would have been " \
                          "2.059722222e1."

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

