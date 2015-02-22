
__problem_title__ = "Arithmetic Derivative"
__problem_url___ = "https://projecteuler.net/problem=484"
__problem_description__ = "The is defined by For example, 20 = 24 Find ∑ ( , ) for 1 < ≤ 5·10 " \
                          "Note: ( , ) denotes the greatest common divisor of and ."

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

