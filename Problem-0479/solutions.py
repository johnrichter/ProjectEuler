
__problem_title__ = "Roots on the Rise"
__problem_url___ = "https://projecteuler.net/problem=479"
__problem_description__ = "Let , , and represent the three solutions (real or complex numbers) " \
                          "to the expression 1/ = ( / ) ( + ) - . For instance, for = 5, we see " \
                          "that { , , } is approximately {5.727244, -0.363622+2.057397i, " \
                          "-0.363622-2.057397i}. Let S( ) = Î£ ( + ) ( + ) ( + ) for all " \
                          "integers , such that 1 â¤ , â¤ . Interestingly, S( ) is always an " \
                          "integer. For example, S(4) = 51160. Find S(10 ) modulo 1 000 000 007."

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

