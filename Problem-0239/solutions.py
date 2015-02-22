
__problem_title__ = "Twenty-two Foolish Primes"
__problem_url___ = "https://projecteuler.net/problem=239"
__problem_description__ = "A set of disks numbered 1 through 100 are placed in a line in random " \
                          "order. What is the probability that we have a partial derangement " \
                          "such that exactly 22 prime number discs are found away from their " \
                          "natural positions? (Any number of non-prime disks may also be found " \
                          "in or out of their natural positions.) Give your answer rounded to 12 " \
                          "places behind the decimal point in the form 0.abcdefghijkl."

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

