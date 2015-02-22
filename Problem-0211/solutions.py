
__problem_title__ = "Divisor Square Sum"
__problem_url___ = "https://projecteuler.net/problem=211"
__problem_description__ = "For a positive integer , let σ ( ) be the sum of the squares of its " \
                          "divisors. For example, Find the sum of all , 0 < < 64,000,000 such " \
                          "that σ ( ) is a perfect square."

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

