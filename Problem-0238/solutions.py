
__problem_title__ = "Infinite string tour"
__problem_url___ = "https://projecteuler.net/problem=238"
__problem_description__ = "Create a sequence of numbers using the "Blum Blum Shub" pseudo-random " \
                          "number generator: Concatenate these numbers … to create a string of " \
                          "infinite length. Then, = For a positive integer , if no substring of " \
                          "exists with a sum of digits equal to , ( ) is defined to be zero. If " \
                          "at least one substring of exists with a sum of digits equal to , we " \
                          "define ( ) = , where is the starting position of the earliest such " \
                          "substring. For instance: The substrings , , , … with respective sums " \
                          "of digits equal to 1, 5, 7, … start at position , hence (1) = (5) = " \
                          "(7) = … = . The substrings , , , … with respective sums of digits " \
                          "equal to 4, 6, 11, … start at position , hence (4) = (6) = (11) = … = " \
                          ". The substrings , , … with respective sums of digits equal to 2, 9, " \
                          "… start at position , hence (2) = (9) = … = . Note that substring " \
                          "starting at position , has a sum of digits equal to 7, but there was " \
                          "an earlier substring (starting at position ) with a sum of digits " \
                          "equal to 7, so (7) = 1, 3. We can verify that, for 0 k ≤ 10 , ∑ ( ) = " \
                          "4742. Find ∑ ( ), for 0 k ≤ 2·10 ."

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

