
__problem_title__ = "Scoring probabilities"
__problem_url___ = "https://projecteuler.net/problem=286"
__problem_description__ = "Barbara is a mathematician and a basketball player. She has found " \
                          "that the probability of scoring a point when shooting from a distance " \
                          "is exactly (1 - / ), where is a real constant greater than 50. During " \
                          "each practice run, she takes shots from distances = 1, = 2, ..., = 50 " \
                          "and, according to her records, she has precisely a 2 % chance to " \
                          "score a total of exactly 20 points. Find and give your answer rounded " \
                          "to 10 decimal places."

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

