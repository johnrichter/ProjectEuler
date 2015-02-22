
__problem_title__ = "Totient maximum"
__problem_url___ = "https://projecteuler.net/problem=69"
__problem_description__ = "Euler's Totient function, φ( ) [sometimes called the phi function], " \
                          "is used to determine the number of numbers less than which are " \
                          "relatively prime to . For example, as 1, 2, 4, 5, 7, and 8, are all " \
                          "less than nine and relatively prime to nine, φ(9)=6. It can be seen " \
                          "that =6 produces a maximum /φ( ) for ≤ 10. Find the value of ≤ " \
                          "1,000,000 for which /φ( ) is a maximum."

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

