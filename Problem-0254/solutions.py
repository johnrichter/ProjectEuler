
__problem_title__ = "Sums of Digit Factorials"
__problem_url___ = "https://projecteuler.net/problem=254"
__problem_description__ = "Define f( ) as the sum of the factorials of the digits of . For " \
                          "example, f(342) = 3! + 4! + 2! = 32. Define sf( ) as the sum of the " \
                          "digits of f( ). So sf(342) = 3 + 2 = 5. Define g( ) to be the " \
                          "smallest positive integer such that sf( ) = . Though sf(342) is 5, " \
                          "sf(25) is also 5, and it can be verified that g(5) is 25. Define sg( " \
                          ") as the sum of the digits of g( ). So sg(5) = 2 + 5 = 7. Further, it " \
                          "can be verified that g(20) is 267 and ∑ sg( ) for 1 ≤ ≤ 20 is 156. " \
                          "What is ∑ sg( ) for 1 ≤ ≤ 150?"

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

