
__problem_title__ = "Diophantine reciprocals III"
__problem_url___ = "https://projecteuler.net/problem=454"
__problem_description__ = "In the following equation , , and are positive integers. For a limit " \
                          "we define F( ) as the number of solutions which satisfy < ≤ . We can " \
                          "verify that F(15) = 4 and F(1000) = 1069. Find F(10 )."

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

