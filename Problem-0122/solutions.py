
__problem_title__ = "Efficient exponentiation"
__problem_url___ = "https://projecteuler.net/problem=122"
__problem_description__ = "The most naive way of computing requires fourteen multiplications: × " \
                          "× ... × = But using a "binary" method you can compute it in six " \
                          "multiplications: × = × = × = × = × = × = However it is yet possible " \
                          "to compute it in only five multiplications: × = × = × = × = × = We " \
                          "shall define m( ) to be the minimum number of multiplications to " \
                          "compute ; for example m(15) = 5. For 1 ≤ ≤ 200, find m( )."

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

