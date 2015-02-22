
__problem_title__ = "Investigating in how many ways objects of two different colours can be grouped"
__problem_url___ = "https://projecteuler.net/problem=181"
__problem_description__ = "Having three black objects B and one white object W they can be " \
                          "grouped in 7 ways like this: In how many ways can sixty black objects " \
                          "B and forty white objects W be thus grouped?"

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

