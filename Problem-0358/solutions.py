
__problem_title__ = "Cyclic numbers"
__problem_url___ = "https://projecteuler.net/problem=358"
__problem_description__ = "A with digits has a very interesting property: When it is multiplied " \
                          "by 1, 2, 3, 4, ... , all the products have exactly the same digits, " \
                          "in the same order, but rotated in a circular fashion! The smallest " \
                          "cyclic number is the 6-digit number 142857 : 142857 × 1 = 142857 " \
                          "142857 × 2 = 285714 142857 × 3 = 428571 142857 × 4 = 571428 142857 × " \
                          "5 = 714285 142857 × 6 = 857142 The next cyclic number is " \
                          "0588235294117647 with 16 digits : 0588235294117647 × 1 = " \
                          "0588235294117647 0588235294117647 × 2 = 1176470588235294 " \
                          "0588235294117647 × 3 = 1764705882352941 ... 0588235294117647 × 16 = " \
                          "9411764705882352 Note that for cyclic numbers, leading zeros are " \
                          "important. There is only one cyclic number for which, the eleven " \
                          "leftmost digits are 00000000137 and the five rightmost digits are " \
                          "56789 (i.e., it has the form 00000000137...56789 with an unknown " \
                          "number of digits in the middle). Find the sum of all its digits."

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

