
__problem_title__ = "Searching for a maximum-sum subsequence"
__problem_url___ = "https://projecteuler.net/problem=149"
__problem_description__ = "Looking at the table below, it is easy to verify that the maximum " \
                          "possible sum of adjacent numbers in any direction (horizontal, " \
                          "vertical, diagonal or anti-diagonal) Now, let us repeat the search, " \
                          "but on a much larger scale: First, generate four million " \
                          "pseudo-random numbers using a specific form of what is known as a " \
                          ""Lagged Fibonacci Generator": For 1 ≤ ≤ 55, = [100003 − 200003 + " \
                          "300007 ] (modulo 1000000) − 500000. For 56 ≤ ≤ 4000000, = [ + + " \
                          "1000000] (modulo 1000000) − 500000. Thus, = −393027 and = 86613. The " \
                          "terms of are then arranged in a 2000×2000 table, using the first 2000 " \
                          "numbers to fill the first row (sequentially), the next 2000 numbers " \
                          "to fill the second row, and so on. Finally, find the greatest sum of " \
                          "(any number of) adjacent entries in any direction (horizontal, " \
                          "vertical, diagonal or anti-diagonal)."

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

