
__problem_title__ = "One-child Numbers"
__problem_url___ = "https://projecteuler.net/problem=413"
__problem_description__ = "We say that a -digit positive number (no leading zeros) is a " \
                          "one-child number if exactly one of its sub-strings is divisible by . " \
                          "For example, 5671 is a 4-digit one-child number. Among all its " \
                          "sub-strings 5, 6, 7, 1, 56, 67, 71, 567, 671 and 5671, only 56 is " \
                          "divisible by 4. Similarly, 104 is a 3-digit one-child number because " \
                          "only 0 is divisible by 3. 1132451 is a 7-digit one-child number " \
                          "because only 245 is divisible by 7. Let F( ) be the number of the " \
                          "one-child numbers less than . We can verify that F(10) = 9, F(10 ) = " \
                          "389 and F(10 ) = 277674. Find F(10 )."

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

