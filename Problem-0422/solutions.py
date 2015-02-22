
__problem_title__ = "Sequence of points on a hyperbola"
__problem_url___ = "https://projecteuler.net/problem=422"
__problem_description__ = "Let H be the hyperbola defined by the equation 12 + 7 - 12 = 625. " \
                          "Next, define X as the point (7, 1). It can be seen that X is in H. " \
                          "Now we define a sequence of points in H, {P : ≥ 1}, as: You are given " \
                          "that P = (-19/2, -229/24), P = (1267/144, -37/12) and P = " \
                          "(17194218091/143327232, 274748766781/1719926784). Find P for = 11 in " \
                          "the following format: If P = ( / , / ) where the fractions are in " \
                          "lowest terms and the denominators are positive, then the answer is ( " \
                          "+ + + ) mod 1 000 000 007. For = 7, the answer would have been: " \
                          "806236837."

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

