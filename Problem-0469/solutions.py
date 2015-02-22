
__problem_title__ = "Empty chairs"
__problem_url___ = "https://projecteuler.net/problem=469"
__problem_description__ = "In a room chairs are placed around a round table. Knights enter the " \
                          "room one by one and choose at random an available empty chair. To " \
                          "have enough elbow room the knights always leave at least one empty " \
                          "chair between each other. When there aren't any suitable chairs left, " \
                          "the fraction of empty chairs is determined. We also define E( ) as " \
                          "the expected value of . We can verify that E(4) = 1/2 and E(6) = 5/9. " \
                          "Find E(10 ). Give your answer rounded to fourteen decimal places in " \
                          "the form 0.abcdefghijklmn."

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

