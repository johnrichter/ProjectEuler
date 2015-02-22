
__problem_title__ = "Comfortable distance"
__problem_url___ = "https://projecteuler.net/problem=364"
__problem_description__ = "There are seats in a row. people come after each other to fill the " \
                          "seats according to the following rules: We can verify that T(10) = " \
                          "61632 and T(1 000) mod 100 000 007 = 47255094. Find T(1 000 000) mod " \
                          "100 000 007."

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

