
__problem_title__ = "Squarefree Numbers"
__problem_url___ = "https://projecteuler.net/problem=193"
__problem_description__ = "A positive integer is called squarefree, if no square of a prime " \
                          "divides , thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree, but not 4, 8, " \
                          "9, 12. How many squarefree numbers are there below 2 ?"

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

