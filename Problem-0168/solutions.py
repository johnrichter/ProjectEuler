
__problem_title__ = "Number Rotations"
__problem_url___ = "https://projecteuler.net/problem=168"
__problem_description__ = "Consider the number 142857. We can right-rotate this number by moving " \
                          "the last digit (7) to the front of it, giving us 714285. It can be " \
                          "verified that 714285=5×142857. This demonstrates an unusual property " \
                          "of 142857: it is a divisor of its right-rotation. Find the last 5 " \
                          "digits of the sum of all integers , 10 < < 10 , that have this " \
                          "property."

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

