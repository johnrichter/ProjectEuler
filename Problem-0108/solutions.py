
__problem_title__ = "Diophantine reciprocals I"
__problem_url___ = "https://projecteuler.net/problem=108"
__problem_description__ = "In the following equation , , and are positive integers. For = 4 " \
                          "there are exactly three distinct solutions: What is the least value " \
                          "of for which the number of distinct solutions exceeds one-thousand? " \
                          "NOTE: This problem is an easier version of ; it is strongly advised " \
                          "that you solve this one first."

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

