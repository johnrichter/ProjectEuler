
__problem_title__ = "Numbers for which Eulerâs totient function equals 13!"
__problem_url___ = "https://projecteuler.net/problem=248"
__problem_description__ = "The first number n for which φ(n)=13! is 6227180929. Find the 150,000 " \
                          "such number."

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

