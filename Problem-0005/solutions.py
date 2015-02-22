
__problem_title__ = "Smallest multiple"
__problem_url___ = "https://projecteuler.net/problem=5"
__problem_description__ = "2520 is the smallest number that can be divided by each of the " \
                          "numbers from 1 to 10 without any remainder. What is the smallest " \
                          "positive number that is by all of the numbers from 1 to 20?"

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

