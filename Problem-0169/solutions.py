
__problem_title__ = "Exploring the number of different ways a number can be expressed as a sum of powers of 2"
__problem_url___ = "https://projecteuler.net/problem=169"
__problem_description__ = "Define f(0)=1 and f( ) to be the number of different ways can be " \
                          "expressed as a sum of integer powers of 2 using each power no more " \
                          "than twice. For example, f(10)=5 since there are five different ways " \
                          "to express 10: 1 + 1 + 8 1 + 1 + 4 + 4 1 + 1 + 2 + 2 + 4 2 + 4 + 4 2 " \
                          "+ 8 What is f(10 )?"

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

