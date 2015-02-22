
__problem_title__ = "Flea Circus"
__problem_url___ = "https://projecteuler.net/problem=213"
__problem_description__ = "A 30×30 grid of squares contains 900 fleas, initially one flea per " \
                          "square. When a bell is rung, each flea jumps to an adjacent square at " \
                          "random (usually 4 possibilities, except for fleas on the edge of the " \
                          "grid or at the corners). What is the expected number of unoccupied " \
                          "squares after 50 rings of the bell? Give your answer rounded to six " \
                          "decimal places."

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

