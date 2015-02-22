
__problem_title__ = "abc-hits"
__problem_url___ = "https://projecteuler.net/problem=127"
__problem_description__ = "The radical of , rad( ), is the product of distinct prime factors of " \
                          ". For example, 504 = 2 × 3 × 7, so rad(504) = 2 × 3 × 7 = 42. We " \
                          "shall define the triplet of positive integers ( , , ) to be an " \
                          "abc-hit if: For example, (5, 27, 32) is an abc-hit, because: It turns " \
                          "out that abc-hits are quite rare and there are only thirty-one " \
                          "abc-hits for < 1000, with ∑ = 12523. Find ∑ for < 120000."

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

