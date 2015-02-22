
__problem_title__ = "Special Pythagorean triplet"
__problem_url___ = "https://projecteuler.net/problem=9"
__problem_description__ = "A Pythagorean triplet is a set of three natural numbers, < < , for " \
                          "which, For example, 3 + 4 = 9 + 16 = 25 = 5 . There exists exactly " \
                          "one Pythagorean triplet for which + + = 1000. Find the product ."

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

