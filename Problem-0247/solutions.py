
__problem_title__ = "Squares under a hyperbola"
__problem_url___ = "https://projecteuler.net/problem=247"
__problem_description__ = "Consider the region constrained by 1 ≤ and 0 ≤ ≤ / . Let S be the " \
                          "largest square that can fit under the curve. Let S be the largest " \
                          "square that fits in the remaining area, and so on. Let the of S be " \
                          "the pair (left, below) indicating the number of squares to the left " \
                          "of S and the number of squares below S . The diagram shows some such " \
                          "squares labelled by number. S has one square to its left and none " \
                          "below, so the index of S is (1,0). It can be seen that the index of S " \
                          "is (1,1) as is the index of S . 50 is the largest for which the index " \
                          "of S is (1,1). What is the largest for which the index of S is (3,3)?"

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

