
__problem_title__ = "Paper sheets of standard sizes: an expected-value problem"
__problem_url___ = "https://projecteuler.net/problem=151"
__problem_description__ = "A printing shop runs 16 batches (jobs) every week and each batch " \
                          "requires a sheet of special colour-proofing paper of size A5. Every " \
                          "Monday morning, the foreman opens a new envelope, containing a large " \
                          "sheet of the special paper with size A1. He proceeds to cut it in " \
                          "half, thus getting two sheets of size A2. Then he cuts one of them in " \
                          "half to get two sheets of size A3 and so on until he obtains the " \
                          "A5-size sheet needed for the first batch of the week. All the unused " \
                          "sheets are placed back in the envelope. At the beginning of each " \
                          "subsequent batch, he takes from the envelope one sheet of paper at " \
                          "random. If it is of size A5, he uses it. If it is larger, he repeats " \
                          "the 'cut-in-half' procedure until he has what he needs and any " \
                          "remaining sheets are always placed back in the envelope. Excluding " \
                          "the first and last batch of the week, find the expected number of " \
                          "times (during each week) that the foreman finds a single sheet of " \
                          "paper in the envelope. Give your answer rounded to six decimal places " \
                          "using the format x.xxxxxx ."

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

