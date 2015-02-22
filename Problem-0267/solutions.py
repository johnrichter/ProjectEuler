
__problem_title__ = "Billionaire"
__problem_url___ = "https://projecteuler.net/problem=267"
__problem_description__ = "You are given a unique investment opportunity. Starting with £1 of " \
                          "capital, you can choose a fixed proportion, , of your capital to bet " \
                          "on a fair coin toss repeatedly for 1000 tosses. Your return is double " \
                          "your bet for heads and you lose your bet for tails. For example, if = " \
                          "1/4, for the first toss you bet £0.25, and if heads comes up you win " \
                          "£0.5 and so then have £1.5. You then bet £0.375 and if the second " \
                          "toss is tails, you have £1.125. Choosing to maximize your chances of " \
                          "having at least £1,000,000,000 after 1,000 flips, what is the chance " \
                          "that you become a billionaire? All computations are assumed to be " \
                          "exact (no rounding), but give your answer rounded to 12 digits behind " \
                          "the decimal point in the form 0.abcdefghijkl."

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

