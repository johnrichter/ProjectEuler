
__problem_title__ = "Arranged probability"
__problem_url___ = "https://projecteuler.net/problem=100"
__problem_description__ = "If a box contains twenty-one coloured discs, composed of fifteen blue " \
                          "discs and six red discs, and two discs were taken at random, it can " \
                          "be seen that the probability of taking two blue discs, P(BB) = " \
                          "(15/21)×(14/20) = 1/2. The next such arrangement, for which there is " \
                          "exactly 50% chance of taking two blue discs at random, is a box " \
                          "containing eighty-five blue discs and thirty-five red discs. By " \
                          "finding the first arrangement to contain over 10 = 1,000,000,000,000 " \
                          "discs in total, determine the number of blue discs that the box would " \
                          "contain."

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

