
__problem_title__ = "Constraining the least greatest and the greatest least"
__problem_url___ = "https://projecteuler.net/problem=350"
__problem_description__ = "A is a sequence of natural numbers. Examples are (2,4,6), (2,6,4), " \
                          "(10,6,15,6), and (11). The , or gcd, of a list is the largest natural " \
                          "number that divides all entries of the list. Examples: gcd(2,6,4) = " \
                          "2, gcd(10,6,15,6) = 1 and gcd(11) = 11. The , or lcm, of a list is " \
                          "the smallest natural number divisible by each entry of the list. " \
                          "Examples: lcm(2,6,4) = 12, lcm(10,6,15,6) = 30 and lcm(11) = 11. Let " \
                          "f( , , ) be the number of lists of size with gcd ≥ and lcm ≤ . For " \
                          "example: f(10, 100, 1) = 91. f(10, 100, 2) = 327. f(10, 100, 3) = " \
                          "1135. f(10, 100, 1000) mod 101 = 3286053. Find f(10 , 10 , 10 ) mod " \
                          "101 ."

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

