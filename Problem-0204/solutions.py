
__problem_title__ = "Generalised Hamming Numbers"
__problem_url___ = "https://projecteuler.net/problem=204"
__problem_description__ = "A Hamming number is a positive number which has no prime factor " \
                          "larger than 5. So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, " \
                          "8, 9, 10, 12, 15. There are 1105 Hamming numbers not exceeding 10 . " \
                          "We will call a positive number a generalised Hamming number of type , " \
                          "if it has no prime factor larger than . Hence the Hamming numbers are " \
                          "the generalised Hamming numbers of type 5. How many generalised " \
                          "Hamming numbers of type 100 are there which don't exceed 10 ?"

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

