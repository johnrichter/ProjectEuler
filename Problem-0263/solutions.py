
__problem_title__ = "An engineers' dream come true"
__problem_url___ = "https://projecteuler.net/problem=263"
__problem_description__ = "Consider the number 6. The divisors of 6 are: 1,2,3 and 6. Every " \
                          "number from 1 up to and including 6 can be written as a sum of " \
                          "distinct divisors of 6: 1=1, 2=2, 3=1+2, 4=1+3, 5=2+3, 6=6. A number " \
                          "is called a practical number if every number from 1 up to and " \
                          "including can be expressed as a sum of distinct divisors of . A pair " \
                          "of consecutive prime numbers with a difference of six is called a " \
                          "sexy pair (since "sex" is the Latin word for "six"). The first sexy " \
                          "pair is (23, 29). We may occasionally find a triple-pair, which means " \
                          "three consecutive sexy prime pairs, such that the second member of " \
                          "each pair is the first member of the next pair. We shall call a " \
                          "number such that : Find the sum of the first four engineers’ " \
                          "paradises."

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

