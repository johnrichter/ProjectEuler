
__problem_title__ = "Cutting Squares"
__problem_url___ = "https://projecteuler.net/problem=270"
__problem_description__ = "A square piece of paper with integer dimensions N×N is placed with a " \
                          "corner at the origin and two of its sides along the - and -axes. " \
                          "Then, we cut it up respecting the following rules: Counting any " \
                          "reflections or rotations as distinct, we call C(N) the number of ways " \
                          "to cut an N×N square. For example, C(1) = 2 and C(2) = 30 (shown " \
                          "below). What is C(30) mod 10 ?"

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

