
__problem_title__ = "Chocolate covered candy"
__problem_url___ = "https://projecteuler.net/problem=449"
__problem_description__ = "Phil the confectioner is making a new batch of chocolate covered " \
                          "candy. Each candy centre is shaped like an ellipsoid of revolution " \
                          "defined by the equation: b + b + a = a b . Phil wants to know how " \
                          "much chocolate is needed to cover one candy centre with a uniform " \
                          "coat of chocolate one millimeter thick. Find the amount of chocolate " \
                          "in mm required if a=3 mm and b=1 mm. Give your answer as the number " \
                          "rounded to 8 decimal places behind the decimal point."

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

