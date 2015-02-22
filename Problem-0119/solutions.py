
__problem_title__ = "Digit power sum"
__problem_url___ = "https://projecteuler.net/problem=119"
__problem_description__ = "The number 512 is interesting because it is equal to the sum of its " \
                          "digits raised to some power: 5 + 1 + 2 = 8, and 8 = 512. Another " \
                          "example of a number with this property is 614656 = 28 . We shall " \
                          "define to be the th term of this sequence and insist that a number " \
                          "must contain at least two digits to have a sum. You are given that = " \
                          "512 and = 614656. Find ."

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

