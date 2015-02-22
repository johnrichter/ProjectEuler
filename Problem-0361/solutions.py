
__problem_title__ = "Subsequence of Thue-Morse sequence"
__problem_url___ = "https://projecteuler.net/problem=361"
__problem_description__ = "The {T } is a binary sequence satisfying: The first several terms of " \
                          "{T } are given as follows: 01101001 1101001011001101001.... We define " \
                          "{A } as the sorted sequence of integers such that the binary " \
                          "expression of each element appears as a subsequence in {T }. For " \
                          "example, the decimal number 18 is expressed as 10010 in binary. 10010 " \
                          "appears in {T } (T to T ), so 18 is an element of {A }. The decimal " \
                          "number 14 is expressed as 1110 in binary. 1110 never appears in {T }, " \
                          "so 14 is not an element of {A }. The first several terms of A are " \
                          "given as follows: We can also verify that A = 3251 and A = " \
                          "80852364498. Find the last 9 digits of ."

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

