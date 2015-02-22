
__problem_title__ = "An ant on the move"
__problem_url___ = "https://projecteuler.net/problem=460"
__problem_description__ = "On the Euclidean plane, an ant travels from point A(0, 1) to point B( " \
                          ", 1) for an integer . In each step, the ant at point ( , ) chooses " \
                          "one of the lattice points ( , ) which satisfy ≥ 0 and ≥ 1 and goes " \
                          "straight to ( , ) at a constant velocity . The value of depends on " \
                          "and as follows: The left image is one of the possible paths for = 4. " \
                          "First the ant goes from A(0, 1) to P (1, 3) at velocity (3 - 1) / " \
                          "(ln(3) - ln(1)) ≈ 1.8205. Then the required time is sqrt(5) / 1.8205 " \
                          "≈ 1.2283. From P (1, 3) to P (3, 3) the ant travels at velocity 3 so " \
                          "the required time is 2 / 3 ≈ 0.6667. From P (3, 3) to B(4, 1) the ant " \
                          "travels at velocity (1 - 3) / (ln(1) - ln(3)) ≈ 1.8205 so the " \
                          "required time is sqrt(5) / 1.8205 ≈ 1.2283. Thus the total required " \
                          "time is 1.2283 + 0.6667 + 1.2283 = 3.1233. The right image is another " \
                          "path. The total required time is calculated as 0.98026 + 1 + 0.98026 " \
                          "= 2.96052. It can be shown that this is the quickest path for = 4. " \
                          "Let F( ) be the total required time if the ant chooses the quickest " \
                          "path. For example, F(4) ≈ 2.960516287. We can verify that F(10) ≈ " \
                          "4.668187834 and F(100) ≈ 9.217221972. Find F(10000). Give your answer " \
                          "rounded to nine decimal places."

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

