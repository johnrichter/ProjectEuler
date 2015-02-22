
__problem_title__ = "A Modified Collatz sequence"
__problem_url___ = "https://projecteuler.net/problem=277"
__problem_description__ = "A modified Collatz sequence of integers is obtained from a starting " \
                          "value a in the following way: = /3 if is divisible by 3. We shall " \
                          "denote this as a large downward step, "D". = (4 + 2)/3 if divided by " \
                          "3 gives a remainder of 1. We shall denote this as an upward step, " \
                          ""U". = (2 - 1)/3 if divided by 3 gives a remainder of 2. We shall " \
                          "denote this as a small downward step, "d". The sequence terminates " \
                          "when some = 1. Given any integer, we can list out the sequence of " \
                          "steps. For instance if =231, then the sequence { " \
                          "}={231,77,51,17,11,7,10,14,9,3,1} corresponds to the steps " \
                          ""DdDddUUdDD". Of course, there are other sequences that begin with " \
                          "that same sequence "DdDddUUdDD....". For instance, if =1004064, then " \
                          "the sequence is DdDddUUdDDDdUDUUUdDdUUDDDUdDD. In fact, 1004064 is " \
                          "the smallest possible > 10 that begins with the sequence DdDddUUdDD. " \
                          "What is the smallest > 10 that begins with the sequence " \
                          ""UDDDUdddDDUDDddDdDddDDUDDdUUDd"?"

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

