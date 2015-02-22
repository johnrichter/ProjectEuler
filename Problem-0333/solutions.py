
__problem_title__ = "Special partitions"
__problem_url___ = "https://projecteuler.net/problem=333"
__problem_description__ = "All positive integers can be partitioned in such a way that each and " \
                          "every term of the partition can be expressed as 2 x3 , where i,j ≥ 0. " \
                          "Let's consider only those such partitions where none of the terms can " \
                          "divide any of the other terms. For example, the partition of 17 = 2 + " \
                          "6 + 9 = (2 x3 + 2 x3 + 2 x3 ) would not be valid since 2 can divide " \
                          "6. Neither would the partition 17 = 16 + 1 = (2 x3 + 2 x3 ) since 1 " \
                          "can divide 16. The only valid partition of 17 would be 8 + 9 = (2 x3 " \
                          "+ 2 x3 ). Many integers have more than one valid partition, the first " \
                          "being 11 having the following two partitions. 11 = 2 + 9 = (2 x3 + 2 " \
                          "x3 ) 11 = 8 + 3 = (2 x3 + 2 x3 ) Let's define P( ) as the number of " \
                          "valid partitions of . For example, P(11) = 2. Let's consider only the " \
                          "prime integers which would have a single valid partition such as " \
                          "P(17). The sum of the primes <100 such that P( )=1 equals 233. Find " \
                          "the sum of the primes <1000000 such that P( )=1."

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

