
__problem_title__ = "Investigating numbers with few repeated digits"
__problem_url___ = "https://projecteuler.net/problem=172"
__problem_description__ = "How many 18-digit numbers (without leading zeros) are there such that " \
                          "no digit occurs more than three times in ?"

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

