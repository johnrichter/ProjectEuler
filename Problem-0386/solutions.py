
__problem_title__ = "Maximum length of an antichain"
__problem_url___ = "https://projecteuler.net/problem=386"
__problem_description__ = "Let be an integer and ( ) be the set of factors of . A subset of ( ) " \
                          "is called an of ( ) if contains only one element or if none of the " \
                          "elements of divides any of the other elements of . For example: (30) " \
                          "= {1, 2, 3, 5, 6, 10, 15, 30} {2, 5, 6} is not an antichain of (30). " \
                          "{2, 3, 5} is an antichain of (30). Let ( ) be the maximum length of " \
                          "an antichain of ( ). Find Σ ( ) for 1 ≤ ≤ 10"

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

