
__problem_title__ = "Range flips"
__problem_url___ = "https://projecteuler.net/problem=430"
__problem_description__ = "disks are placed in a row, indexed 1 to from left to right. Each disk " \
                          "has a black side and white side. Initially all disks show their white " \
                          "side. At each turn, two, not necessarily distinct, integers and " \
                          "between 1 and (inclusive) are chosen uniformly at random. All disks " \
                          "with an index from to (inclusive) are flipped. The following example " \
                          "shows the case = 8. At the first turn = 5 and = 2, and at the second " \
                          "turn = 4 and = 6. Let E( , ) be the expected number of disks that " \
                          "show their white side after turns. We can verify that E(3, 1) = 10/9, " \
                          "E(3, 2) = 5/3, E(10, 4) ≈ 5.157 and E(100, 10) ≈ 51.893. Find E(10 , " \
                          "4000). Give your answer rounded to 2 decimal places behind the " \
                          "decimal point."

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

