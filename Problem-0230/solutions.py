
__problem_title__ = "Fibonacci Words"
__problem_url___ = "https://projecteuler.net/problem=230"
__problem_description__ = "For any two strings of digits, A and B, we define F to be the " \
                          "sequence (A,B,AB,BAB,ABBAB,...) in which each term is the " \
                          "concatenation of the previous two. Further, we define D ( ) to be the " \
                          "digit in the first term of F that contains at least digits. Example: " \
                          "Let A=1415926535, B=8979323846. We wish to find D (35), say. The " \
                          "first few terms of F are: 1415926535 8979323846 14159265358979323846 " \
                          "897932384614159265358979323846 1415926535897932384689793238461415 " \
                          "265358979323846 Then D (35) is the 35 digit in the fifth term, which " \
                          "is 9. Now we use for A the first 100 digits of π behind the decimal " \
                          "point: 14159265358979323846264338327950288419716939937510 " \
                          "58209749445923078164062862089986280348253421170679 and for B the next " \
                          "hundred digits: 82148086513282306647093844609550582231725359408128 " \
                          "48111745028410270193852110555964462294895493038196 . Find ∑ 10 × D " \
                          "((127+19 )×7 ) ."

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

