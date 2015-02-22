
__problem_title__ = "Pandigital prime"
__problem_url___ = "https://projecteuler.net/problem=41"
__problem_description__ = "We shall say that an -digit number is pandigital if it makes use of " \
                          "all the digits 1 to exactly once. For example, 2143 is a 4-digit " \
                          "pandigital and is also prime. What is the largest -digit pandigital " \
                          "prime that exists?"

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

