
__problem_title__ = "Exploring Pascal's pyramid"
__problem_url___ = "https://projecteuler.net/problem=154"
__problem_description__ = "A triangular pyramid is constructed using spherical balls so that " \
                          "each ball rests on exactly three balls of the next lower level. Then, " \
                          "we calculate the number of paths leading from the apex to each " \
                          "position: A path starts at the apex and progresses downwards to any " \
                          "of the three spheres directly below the current position. " \
                          "Consequently, the number of paths to reach a certain position is the " \
                          "sum of the numbers immediately above it (depending on the position, " \
                          "there are up to three numbers above it). The result is and the " \
                          "numbers at each level are the coefficients of the trinomial expansion " \
                          "( ) . How many coefficients in the expansion of ( ) are multiples of " \
                          "10 ?"

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

