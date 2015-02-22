
__problem_title__ = "Counting block combinations I"
__problem_url___ = "https://projecteuler.net/problem=114"
__problem_description__ = "A row measuring seven units in length has red blocks with a minimum " \
                          "length of three units placed on it, such that any two red blocks " \
                          "(which are allowed to be different lengths) are separated by at least " \
                          "one black square. There are exactly seventeen ways of doing this. How " \
                          "many ways can a row measuring fifty units in length be filled? NOTE: " \
                          "Although the example above does not lend itself to the possibility, " \
                          "in general it is permitted to mix block sizes. For example, on a row " \
                          "measuring eight units in length you could use red (3), black (1), and " \
                          "red (4)."

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

