
__problem_title__ = "Prime pair sets"
__problem_url___ = "https://projecteuler.net/problem=60"
__problem_description__ = "The primes 3, 7, 109, and 673, are quite remarkable. By taking any " \
                          "two primes and concatenating them in any order the result will always " \
                          "be prime. For example, taking 7 and 109, both 7109 and 1097 are " \
                          "prime. The sum of these four primes, 792, represents the lowest sum " \
                          "for a set of four primes with this property. Find the lowest sum for " \
                          "a set of five primes for which any two primes concatenate to produce " \
                          "another prime."

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

