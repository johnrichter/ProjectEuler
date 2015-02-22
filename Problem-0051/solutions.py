
__problem_title__ = "Prime digit replacements"
__problem_url___ = "https://projecteuler.net/problem=51"
__problem_description__ = "By replacing the 1 digit of the 2-digit number *3, it turns out that " \
                          "six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all " \
                          "prime. By replacing the 3 and 4 digits of 56**3 with the same digit, " \
                          "this 5-digit number is the first example having seven primes among " \
                          "the ten generated numbers, yielding the family: 56003, 56113, 56333, " \
                          "56443, 56663, 56773, and 56993. Consequently 56003, being the first " \
                          "member of this family, is the smallest prime with this property. Find " \
                          "the smallest prime which, by replacing part of the number (not " \
                          "necessarily adjacent digits) with the same digit, is part of an eight " \
                          "prime value family."

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

