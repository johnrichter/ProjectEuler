
__problem_title__ = "Numbers in decimal expansions"
__problem_url___ = "https://projecteuler.net/problem=316"
__problem_description__ = "Let = ... be an infinite sequence of random digits, selected from " \
                          "{0,1,2,3,4,5,6,7,8,9} with equal probability. It can be seen that " \
                          "corresponds to the real number 0. .... It can also be seen that " \
                          "choosing a random real number from the interval [0,1) is equivalent " \
                          "to choosing an infinite sequence of random digits selected from " \
                          "{0,1,2,3,4,5,6,7,8,9} with equal probability. For any positive " \
                          "integer with decimal digits, let be the smallest index such that , " \
                          "... are the decimal digits of , in the same order. Also, let ( ) be " \
                          "the expected value of ; it can be proven that ( ) is always finite " \
                          "and, interestingly, always an integer number. For example, if = 535, " \
                          "then for = 31415926 897...., we get = 9 for = " \
                          "35528714365004956000049084876408468 4..., we get = 36 etc and we find " \
                          "that (535) = 1008. Given that , find"

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

