
__problem_title__ = "Counting Digits"
__problem_url___ = "https://projecteuler.net/problem=156"
__problem_description__ = "Starting from zero the natural numbers are written down in base 10 " \
                          "like this: 0 1 2 3 4 5 6 7 8 9 10 11 12.... Consider the digit =1. " \
                          "After we write down each number , we will update the number of ones " \
                          "that have occurred and call this number ( ,1). The first values for ( " \
                          ",1), then, are as follows: Note that ( ,1) never equals 3. So the " \
                          "first two solutions of the equation ( ,1)= are =0 and =1. The next " \
                          "solution is =199981. In the same manner the function ( ) gives the " \
                          "total number of digits that have been written down after the number " \
                          "has been written. In fact, for every digit ≠ 0, 0 is the first " \
                          "solution of the equation ( )= . Let ( ) be the sum of all the " \
                          "solutions for which ( )= . You are given that (1)=22786974071. Find ∑ " \
                          "( ) for 1 ≤ d ≤ 9. Note: if, for some , ( )= for more than one value " \
                          "of this value of is counted again for every value of for which ( )= ."

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

