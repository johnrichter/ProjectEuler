
__problem_title__ = "Investigating the behaviour of a recursively defined sequence"
__problem_url___ = "https://projecteuler.net/problem=197"
__problem_description__ = "Given is the function ( ) = ⌊2 ⌋ × 10 ( ⌊ ⌋ is the floor-function), " \
                          "the sequence is defined by = -1 and = ( ). Find + for = 10 . Give " \
                          "your answer with 9 digits after the decimal point."

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

