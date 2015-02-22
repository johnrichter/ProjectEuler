
__problem_title__ = "Superinteger"
__problem_url___ = "https://projecteuler.net/problem=467"
__problem_description__ = "An integer is called a of another integer if the digits of form a of " \
                          "the digits of . For example, 2718281828 is a superinteger of 18828, " \
                          "while 314159 is not a superinteger of 151. Let ( ) be the th prime " \
                          "number, and let ( ) be the th composite number. For example, (1) = 2, " \
                          "(10) = 29, (1) = 4 and (10) = 18. { ( ) : i ≥ 1} = {2, 3, 5, 7, 11, " \
                          "13, 17, 19, 23, 29, ...} { ( ) : i ≥ 1} = {4, 6, 8, 9, 10, 12, 14, " \
                          "15, 16, 18, ...} Let P the sequence of the of { ( )} (C is defined " \
                          "similarly for { ( )}): P = {2, 3, 5, 7, 2, 4, 8, 1, 5, 2, ...} C = " \
                          "{4, 6, 8, 9, 1, 3, 5, 6, 7, 9, ...} Let P be the integer formed by " \
                          "concatenating the first elements of P (C is defined similarly for C " \
                          "). P = 2357248152 C = 4689135679 Let ( ) be the smallest positive " \
                          "integer that is a common superinteger of P and C . For example, (10) " \
                          "= 2357246891352679, and (100) mod 1 000 000 007 = 771661825. Find (10 " \
                          "000) mod 1 000 000 007."

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

