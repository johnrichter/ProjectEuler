
__problem_title__ = "Look and say sequence"
__problem_url___ = "https://projecteuler.net/problem=419"
__problem_description__ = "The sequence goes 1, 11, 21, 1211, 111221, 312211, 13112221, " \
                          "1113213211, ... The sequence starts with 1 and all other members are " \
                          "obtained by describing the previous member in terms of consecutive " \
                          "digits. It helps to do this out loud: 1 is 'one one' → 11 11 is 'two " \
                          "ones' → 21 21 is 'one two and one one' → 1211 1211 is 'one one, one " \
                          "two and two ones' → 111221 111221 is 'three ones, two twos and one " \
                          "one' → 312211 ... Define A(n), B(n) and C(n) as the number of ones, " \
                          "twos and threes in the n'th element of the sequence respectively. One " \
                          "can verify that A(40) = 31254, B(40) = 20259 and C(40) = 11625. Find " \
                          "A(n), B(n) and C(n) for n = 10 . Give your answer modulo 2 and " \
                          "separate your values for A, B and C by a comma. E.g. for n = 40 the " \
                          "answer would be 31254,20259,11625"

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

