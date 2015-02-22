
__problem_title__ = "Prime square remainders"
__problem_url___ = "https://projecteuler.net/problem=123"
__problem_description__ = "Let be the th prime: 2, 3, 5, 7, 11, ..., and let be the remainder " \
                          "when ( −1) + ( +1) is divided by . For example, when = 3, = 5, and 4 " \
                          "+ 6 = 280 ≡ 5 mod 25. The least value of for which the remainder " \
                          "first exceeds 10 is 7037. Find the least value of for which the " \
                          "remainder first exceeds 10 ."

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

