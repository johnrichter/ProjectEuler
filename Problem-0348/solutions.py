
__problem_title__ = "Sum of a square and a cube"
__problem_url___ = "https://projecteuler.net/problem=348"
__problem_description__ = "Many numbers can be expressed as the sum of a square and a cube. Some " \
                          "of them in more than one way. Consider the palindromic numbers that " \
                          "can be expressed as the sum of a square and a cube, both greater than " \
                          "1, in 4 different ways. For example, 5229225 is a palindromic number " \
                          "and it can be expressed in exactly 4 different ways: 2285 + 20 2223 + " \
                          "66 1810 + 125 1197 + 156 Find the sum of the five smallest such " \
                          "palindromic numbers."

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

