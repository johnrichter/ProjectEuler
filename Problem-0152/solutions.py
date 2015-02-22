
__problem_title__ = "Writing 1/2 as a sum of inverse squares"
__problem_url___ = "https://projecteuler.net/problem=152"
__problem_description__ = "There are several ways to write the number 1/2 as a sum of inverse " \
                          "squares using integers. For instance, the numbers " \
                          "{2,3,4,5,7,12,15,20,28,35} can be used: In fact, only using integers " \
                          "between 2 and 45 inclusive, there are exactly three ways to do it, " \
                          "the remaining two being: {2,3,4,6,7,9,10,20,28,35,36,45} and " \
                          "{2,3,4,6,7,9,12,15,28,30,35,36,45}. How many ways are there to write " \
                          "the number 1/2 as a sum of inverse squares using distinct integers " \
                          "between 2 and 80 inclusive?"

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

