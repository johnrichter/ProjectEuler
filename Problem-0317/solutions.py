
__problem_title__ = "Firecracker"
__problem_url___ = "https://projecteuler.net/problem=317"
__problem_description__ = "A firecracker explodes at a height of 100 m above level ground. It " \
                          "breaks into a large number of very small fragments, which move in " \
                          "every direction; all of them have the same initial velocity of 20 " \
                          "m/s. We assume that the fragments move without air resistance, in a " \
                          "uniform gravitational field with g=9.81 m/s . Find the volume (in m ) " \
                          "of the region through which the fragments move before reaching the " \
                          "ground. Give your answer rounded to four decimal places."

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

