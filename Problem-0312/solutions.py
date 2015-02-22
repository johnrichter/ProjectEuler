
__problem_title__ = "Cyclic paths on SierpiÅski graphs"
__problem_url___ = "https://projecteuler.net/problem=312"
__problem_description__ = "- A of order-1 ( ) is an equilateral triangle. - is obtained from by " \
                          "positioning three copies of so that every pair of copies has one " \
                          "common corner. Let C( ) be the number of cycles that pass exactly " \
                          "once through all the vertices of . For example, C(3) = 8 because " \
                          "eight such cycles can be drawn on , as shown below: It can also be " \
                          "verified that : C(1) = C(2) = 1 C(5) = 71328803586048 C(10 000) mod " \
                          "10 = 37652224 C(10 000) mod 13 = 617720485 Find C(C(C(10 000))) mod " \
                          "13 ."

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

