
__problem_title__ = "Pentagon numbers"
__problem_url___ = "https://projecteuler.net/problem=44"
__problem_description__ = "Pentagonal numbers are generated by the formula, P = (3 −1)/2. The " \
                          "first ten pentagonal numbers are: 1, 5, 12, 22, 35, 51, 70, 92, 117, " \
                          "145, ... It can be seen that P + P = 22 + 70 = 92 = P . However, " \
                          "their difference, 70 − 22 = 48, is not pentagonal. Find the pair of " \
                          "pentagonal numbers, P and P , for which their sum and difference are " \
                          "pentagonal and D = |P − P | is minimised; what is the value of D?"

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

