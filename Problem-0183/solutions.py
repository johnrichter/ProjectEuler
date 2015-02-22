
__problem_title__ = "Maximum product of parts"
__problem_url___ = "https://projecteuler.net/problem=183"
__problem_description__ = "Let N be a positive integer and let N be split into equal parts, = N/ " \
                          ", so that N = + + ... + . Let P be the product of these parts, P = × " \
                          "× ... × = . For example, if 11 is split into five equal parts, 11 = " \
                          "2.2 + 2.2 + 2.2 + 2.2 + 2.2, then P = 2.2 = 51.53632. Let M(N) = P " \
                          "for a given value of N. It turns out that the maximum for N = 11 is " \
                          "found by splitting eleven into four equal parts which leads to P = " \
                          "(11/4) ; that is, M(11) = 14641/256 = 57.19140625, which is a " \
                          "terminating decimal. However, for N = 8 the maximum is achieved by " \
                          "splitting it into three equal parts, so M(8) = 512/27, which is a " \
                          "non-terminating decimal. Let D(N) = N if M(N) is a non-terminating " \
                          "decimal and D(N) = -N if M(N) is a terminating decimal. For example, " \
                          "ΣD(N) for 5 ≤ N ≤ 100 is 2438. Find ΣD(N) for 5 ≤ N ≤ 10000."

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

