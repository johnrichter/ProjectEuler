
__problem_title__ = "Modular Cubes, part 1"
__problem_url___ = "https://projecteuler.net/problem=271"
__problem_description__ = "For a positive number , define S( ) as the sum of the integers for " \
                          "which 1< < and ≡1 mod . When =91, there are 8 possible values for , " \
                          "namely : 9, 16, 22, 29, 53, 74, 79, 81. Thus, " \
                          "S(91)=9+16+22+29+53+74+79+81=363. Find S(13082761331670030)."

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

