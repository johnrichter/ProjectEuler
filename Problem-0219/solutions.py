
__problem_title__ = "Skew-cost coding"
__problem_url___ = "https://projecteuler.net/problem=219"
__problem_description__ = "Let and be bit strings (sequences of 0's and 1's). If is equal to the " \
                          "most length( ) bits of , then is said to be a of . For example, 00110 " \
                          "is a prefix of 1001, but not of 00111 or 100110. A is a collection of " \
                          "distinct bit strings such that no string is a prefix of any other. " \
                          "For example, this is a prefix-free code of size 6: 0000, 0001, 001, " \
                          "01, 10, 11 Now suppose that it costs one penny to transmit a '0' bit, " \
                          "but four pence to transmit a '1'. Then the total cost of the " \
                          "prefix-free code shown above is 35 pence, which happens to be the " \
                          "cheapest possible for the skewed pricing scheme in question. In " \
                          "short, we write Cost(6) = 35. What is Cost(10 ) ?"

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

