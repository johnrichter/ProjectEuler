
__problem_title__ = "n-sequences"
__problem_url___ = "https://projecteuler.net/problem=427"
__problem_description__ = "A sequence of integers S = {s } is called an if it has elements and " \
                          "each element s satisfies 1 ≤ s ≤ . Thus there are distinct -sequences " \
                          "in total. For example, the sequence S = {1, 5, 5, 10, 7, 7, 7, 2, 3, " \
                          "7} is a 10-sequence. For any sequence S, let L(S) be the length of " \
                          "the longest contiguous subsequence of S with the same value. For " \
                          "example, for the given sequence S above, L(S) = 3, because of the " \
                          "three consecutive 7's. Let ( ) = ∑ L(S) for all -sequences S. For " \
                          "example, (3) = 45, (7) = 1403689 and (11) = 481496895121. Find (7 500 " \
                          "000) mod 1 000 000 009."

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

