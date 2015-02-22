
__problem_title__ = "The totient of a square is a cube"
__problem_url___ = "https://projecteuler.net/problem=342"
__problem_description__ = "Consider the number 50. 50 = 2500 = 2 × 5 , so φ(2500) = 2 × 4 × 5 = " \
                          "8 × 5 = 2 × 5 . So 2500 is a square and φ(2500) is a cube. Find the " \
                          "sum of all numbers n, 1 &lt n < 10 such that φ(n ) is a cube. φ " \
                          "denotes ."

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

