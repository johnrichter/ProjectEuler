
__problem_title__ = "Number spiral diagonals"
__problem_url___ = "https://projecteuler.net/problem=28"
__problem_description__ = "Starting with the number 1 and moving to the right in a clockwise " \
                          "direction a 5 by 5 spiral is formed as follows: 22 23 24 20 8 10 19 6 " \
                          "2 11 18 4 12 16 15 14 It can be verified that the sum of the numbers " \
                          "on the diagonals is 101. What is the sum of the numbers on the " \
                          "diagonals in a 1001 by 1001 spiral formed in the same way?"

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

