
__problem_title__ = "Tidying up"
__problem_url___ = "https://projecteuler.net/problem=253"
__problem_description__ = "A small child has a “number caterpillar” consisting of forty jigsaw " \
                          "pieces, each with one number on it, which, when connected together in " \
                          "a line, reveal the numbers 1 to 40 in order. Every night, the child's " \
                          "father has to pick up the pieces of the caterpillar that have been " \
                          "scattered across the play room. He picks up the pieces at random and " \
                          "places them in the correct order. As the caterpillar is built up in " \
                          "this way, it forms distinct segments that gradually merge together. " \
                          "The number of segments starts at zero (no pieces placed), generally " \
                          "increases up to about eleven or twelve, then tends to drop again " \
                          "before finishing at a single segment (all pieces placed). For " \
                          "example: Let be the maximum number of segments encountered during a " \
                          "random tidy-up of the caterpillar. For a caterpillar of ten pieces, " \
                          "the number of possibilities for each is so the most likely value of " \
                          "is 3 and the average value is ⁄ = 3.400732, rounded to six decimal " \
                          "places. The most likely value of for a forty-piece caterpillar is 11; " \
                          "but what is the average value of ? Give your answer rounded to six " \
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

