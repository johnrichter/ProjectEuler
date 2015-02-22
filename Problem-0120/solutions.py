
__problem_title__ = "Square remainders"
__problem_url___ = "https://projecteuler.net/problem=120"
__problem_description__ = "Let be the remainder when ( −1) + ( +1) is divided by . For example, " \
                          "if = 7 and = 3, then = 42: 6 + 8 = 728 ≡ 42 mod 49. And as varies, so " \
                          "too will , but for = 7 it turns out that = 42. For 3 ≤ ≤ 1000, find ."

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

