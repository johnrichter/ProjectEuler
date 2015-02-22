
__problem_title__ = "Collatz prefix families"
__problem_url___ = "https://projecteuler.net/problem=494"
__problem_description__ = "The Collatz sequence is defined as: $a_{i+1} = \left\{ \large{\frac " \
                          "{a_i} 2 \atop 3 a_i+1} {\text{if }a_i\text{ is even} \atop \text{if " \
                          "}a_i\text{ is odd}} \right.$. The Collatz conjecture states that " \
                          "starting from any positive integer, the sequence eventually reaches " \
                          "the cycle 1,4,2,1.... We shall define the sequence prefix for the " \
                          "Collatz sequence starting with as the sub-sequence of all numbers not " \
                          "a power of 2 (2 =1 is considered a power of 2 for this problem). For " \
                          "example: (13) = {13, 40, 20, 10, 5} (8) = {} Any number invalidating " \
                          "the conjecture would have an infinite length sequence prefix. Let be " \
                          "the set of all sequence prefixes of length . Two sequences {a , a , " \
                          "..., a } and {b , b , ..., b } in are said to belong to the same " \
                          "prefix family if a j if and only if b j for all 1 ≤ i,j ≤ . For " \
                          "example, in , {6, 3, 10, 5} is in the same family as {454, 227, 682, " \
                          "341}, but not {113, 340, 170, 85}. Let be the number of distinct " \
                          "prefix families in . You are given (5) = 5, (10) = 55, (20) = 6771. " \
                          "Find f(90)."

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

