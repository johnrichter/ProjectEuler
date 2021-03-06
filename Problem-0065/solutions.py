
__problem_title__ = "Convergents of e"
__problem_url___ = "https://projecteuler.net/problem=65"
__problem_description__ = "The square root of 2 can be written as an infinite continued " \
                          "fraction. The infinite continued fraction can be written, √2 = " \
                          "[1;(2)], (2) indicates that 2 repeats . In a similar way, √23 = " \
                          "[4;(1,3,1,8)]. It turns out that the sequence of partial values of " \
                          "continued fractions for square roots provide the best rational " \
                          "approximations. Let us consider the convergents for √2. Hence the " \
                          "sequence of the first ten convergents for √2 are: What is most " \
                          "surprising is that the important mathematical constant, = [2; 1,2,1, " \
                          "1,4,1, 1,6,1 , ... , 1,2 ,1, ...]. The first ten terms in the " \
                          "sequence of convergents for are: The sum of digits in the numerator " \
                          "of the 10 convergent is 1+4+5+7=17. Find the sum of digits in the " \
                          "numerator of the 100 convergent of the continued fraction for ."

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

