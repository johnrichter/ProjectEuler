
__problem_title__ = "Ambiguous Numbers"
__problem_url___ = "https://projecteuler.net/problem=198"
__problem_description__ = "A best approximation to a real number for the denominator bound is a " \
                          "rational number / (in reduced form) with ≤ , so that any rational " \
                          "number / which is closer to than / has > . Usually the best " \
                          "approximation to a real number is uniquely determined for all " \
                          "denominator bounds. However, there are some exceptions, e.g. 9/40 has " \
                          "the two best approximations 1/4 and 1/5 for the denominator bound 6. " \
                          "We shall call a real number , if there is at least one denominator " \
                          "bound for which possesses two best approximations. Clearly, an " \
                          "ambiguous number is necessarily rational. How many ambiguous numbers " \
                          "= / , 0 < < 1/100, are there whose denominator does not exceed 10 ?"

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

