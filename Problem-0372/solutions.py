
__problem_title__ = "Pencils of rays"
__problem_url___ = "https://projecteuler.net/problem=372"
__problem_description__ = "Let R( , ) be the number of lattice points ( , ) which satisfy < ≤ , " \
                          "< ≤ and is odd. We can verify that R(0, 100) = 3019 and R(100, 10000) " \
                          "= 29750422. Find R(2·10 , 10 ). : represents the floor function."

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

