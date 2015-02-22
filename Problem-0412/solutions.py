
__problem_title__ = "Gnomon numbering"
__problem_url___ = "https://projecteuler.net/problem=412"
__problem_description__ = "For integers , (0 ≤ m), let L( , ) be an × grid with the top-right × " \
                          "grid removed. For example, L(5, 3) looks like this: We want to number " \
                          "each cell of L( , ) with consecutive integers 1, 2, 3, ... such that " \
                          "the number in every cell is smaller than the number below it and to " \
                          "the left of it. For example, here are two valid numberings of L(5, " \
                          "3): Let LC( , ) be the number of valid numberings of L( , ). It can " \
                          "be verified that LC(3, 0) = 42, LC(5, 3) = 250250, LC(6, 3) = " \
                          "406029023400 and LC(10, 5) mod 76543217 = 61251715. Find LC(10000, " \
                          "5000) mod 76543217."

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

