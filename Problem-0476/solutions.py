
__problem_title__ = "Circle Packing II"
__problem_url___ = "https://projecteuler.net/problem=476"
__problem_description__ = "Let ( , , ) be the maximum area covered by three non-overlapping " \
                          "circles inside a triangle with edge lengths , and . Let ( ) be the " \
                          "average value of ( , , ) over all integer triplets ( , , ) such that " \
                          "1 ≤ ≤ ≤ a + ≤ You are given (2) = (1, 1, 1) â 0.31998, (5) â " \
                          "1.25899. Find (1803) rounded to 5 decimal places behind the decimal " \
                          "point."

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

