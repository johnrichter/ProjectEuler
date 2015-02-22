
__problem_title__ = "Goldbach's other conjecture"
__problem_url___ = "https://projecteuler.net/problem=46"
__problem_description__ = "It was proposed by Christian Goldbach that every odd composite number " \
                          "can be written as the sum of a prime and twice a square. 9 = 7 + 2×1 " \
                          "15 = 7 + 2×2 21 = 3 + 2×3 25 = 7 + 2×3 27 = 19 + 2×2 33 = 31 + 2×1 It " \
                          "turns out that the conjecture was false. What is the smallest odd " \
                          "composite that cannot be written as the sum of a prime and twice a " \
                          "square?"

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

