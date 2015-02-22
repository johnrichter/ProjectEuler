
__problem_title__ = "A Kempner-like series"
__problem_url___ = "https://projecteuler.net/problem=368"
__problem_description__ = "If we however omit from this series every term where the denominator " \
                          "has a 9 in it, the series remarkably enough converges to " \
                          "approximately 22.9206766193. This modified harmonic series is called " \
                          "the series. Let us now consider another modified harmonic series by " \
                          "omitting from the harmonic series every term where the denominator " \
                          "has 3 or more equal consecutive digits. One can verify that out of " \
                          "the first 1200 terms of the harmonic series, only 20 terms will be " \
                          "omitted. These 20 omitted terms are: This series converges as well. " \
                          "Find the value the series converges to. Give your answer rounded to " \
                          "10 digits behind the decimal point."

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

