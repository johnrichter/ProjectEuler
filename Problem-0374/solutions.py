
__problem_title__ = "Maximum Integer Partition Product"
__problem_url___ = "https://projecteuler.net/problem=374"
__problem_description__ = "An integer partition of a number is a way of writing as a sum of " \
                          "positive integers. Partitions that differ only in the order of their " \
                          "summands are considered the same. A partition of into is a partition " \
                          "of in which every part occurs at most once. The partitions of 5 into " \
                          "distinct parts are: 5, 4+1 and 3+2. Let f( ) be the maximum product " \
                          "of the parts of any such partition of into distinct parts and let m( " \
                          ") be the number of elements of any such partition of with that " \
                          "product. So f(5)=6 and m(5)=2. For =10 the partition with the largest " \
                          "product is 10=2+3+5, which gives f(10)=30 and m(10)=3. And their " \
                          "product, f(10)·m(10) = 30·3 = 90 It can be verified that ∑f( )·m( ) " \
                          "for 1 ≤ ≤ 100 = 1683550844462. Find ∑f( )·m( ) for 1 ≤ ≤ 10 . Give " \
                          "your answer modulo 982451653, the 50 millionth prime."

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

