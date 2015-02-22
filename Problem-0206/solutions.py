
__problem_title__ = "Concealed Square"
__problem_url___ = "https://projecteuler.net/problem=206"
__problem_description__ = "Find the unique positive integer whose square has the form " \
                          "1_2_3_4_5_6_7_8_9_0, where each “_” is a single digit."

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

