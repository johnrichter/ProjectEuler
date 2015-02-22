
__problem_title__ = "(prime-k) factorial"
__problem_url___ = "https://projecteuler.net/problem=381"
__problem_description__ = "For a prime p let S(p) = (∑(p-k)!) mod(p) for 1 ≤ k ≤ 5. For example, " \
                          "if p=7, (7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + " \
                          "3! + 2! = 720+120+24+6+2 = 872. As 872 mod(7) = 4, S(7) = 4. It can " \
                          "be verified that ∑S(p) = 480 for 5 ≤ p < 100. Find ∑S(p) for 5 ≤ p < " \
                          "10 ."

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

