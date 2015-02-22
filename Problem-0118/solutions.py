
__problem_title__ = "Pandigital prime sets"
__problem_url___ = "https://projecteuler.net/problem=118"
__problem_description__ = "Using all of the digits 1 through 9 and concatenating them freely to " \
                          "form decimal integers, different sets can be formed. Interestingly " \
                          "with the set {2,5,47,89,631}, all of the elements belonging to it are " \
                          "prime. How many distinct sets containing each of the digits one " \
                          "through nine exactly once contain only prime elements?"

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

