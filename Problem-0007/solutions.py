
__problem_title__ = "10001st prime"
__problem_url___ = "https://projecteuler.net/problem=7"
__problem_description__ = "By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we " \
                          "can see that the 6th prime is 13. What is the 10 001st prime number?"

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

