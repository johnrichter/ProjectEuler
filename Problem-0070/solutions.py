
__problem_title__ = "Totient permutation"
__problem_url___ = "https://projecteuler.net/problem=70"
__problem_description__ = "Euler's Totient function, φ( ) [sometimes called the phi function], " \
                          "is used to determine the number of positive numbers less than or " \
                          "equal to which are relatively prime to . For example, as 1, 2, 4, 5, " \
                          "7, and 8, are all less than nine and relatively prime to nine, " \
                          "φ(9)=6. The number 1 is considered to be relatively prime to every " \
                          "positive number, so φ(1)=1. Interestingly, φ(87109)=79180, and it can " \
                          "be seen that 87109 is a permutation of 79180. Find the value of , 1 < " \
                          "< 10 , for which φ( ) is a permutation of and the ratio /φ( ) " \
                          "produces a minimum."

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

