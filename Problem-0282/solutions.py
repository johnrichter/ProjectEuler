
__problem_title__ = "The Ackermann function"
__problem_url___ = "https://projecteuler.net/problem=282"
__problem_description__ = "For non-negative integers , , the Ackermann function ( , ) is defined " \
                          "as follows: For example (1, 0) = 2, (2, 2) = 7 and (3, 4) = 125. Find " \
                          "( , ) and give your answer mod 14 ."

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

