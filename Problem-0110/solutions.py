
__problem_title__ = "Diophantine reciprocals II"
__problem_url___ = "https://projecteuler.net/problem=110"
__problem_description__ = "In the following equation , , and are positive integers. It can be " \
                          "verified that when = 1260 there are 113 distinct solutions and this " \
                          "is the least value of for which the total number of distinct " \
                          "solutions exceeds one hundred. What is the least value of for which " \
                          "the number of distinct solutions exceeds four million? NOTE: This " \
                          "problem is a much more difficult version of and as it is well beyond " \
                          "the limitations of a brute force approach it requires a clever " \
                          "implementation."

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

