
__problem_title__ = "Best Approximations"
__problem_url___ = "https://projecteuler.net/problem=192"
__problem_description__ = "Let be a real number. A to for the is a rational number / , with ≤ , " \
                          "such that any rational number which is closer to than / has a " \
                          "denominator larger than : For example, the best approximation to √13 " \
                          "for the denominator bound 20 is 18/5 and the best approximation to " \
                          "√13 for the denominator bound 30 is 101/28. Find the sum of all " \
                          "denominators of the best approximations to √ for the denominator " \
                          "bound 10 , where is not a perfect square and 1 < ≤ 100000."

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

