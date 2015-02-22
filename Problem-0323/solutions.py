
__problem_title__ = "Bitwise-OR operations on random integers"
__problem_url___ = "https://projecteuler.net/problem=323"
__problem_description__ = "Let , , ,... be a sequence of random unsigned 32 bit integers (i.e. 0 " \
                          "≤ < 2 , every value equally likely). For the sequence the following " \
                          "recursion is given: It can be seen that eventually there will be an " \
                          "index N such that = 2 -1 (a bit-pattern of all ones) for all ≥ N. " \
                          "Find the expected value of N. Give your answer rounded to 10 digits " \
                          "after the decimal point."

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

