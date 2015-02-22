
__problem_title__ = "Multiples with small digits"
__problem_url___ = "https://projecteuler.net/problem=303"
__problem_description__ = "For a positive integer , define ( ) as the least positive multiple of " \
                          "that, written in base 10, uses only digits ≤ 2. Thus (2)=2, (3)=12, " \
                          "(7)=21, (42)=210, (89)=1121222. Also, . Find ."

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

