
__problem_title__ = "Rounded Square Roots"
__problem_url___ = "https://projecteuler.net/problem=255"
__problem_description__ = "We define the of a positive integer as the square root of rounded to " \
                          "the nearest integer. The following procedure (essentially Heron's " \
                          "method adapted to integer arithmetic) finds the rounded-square-root " \
                          "of : Let be the number of digits of the number . If is odd, set = " \
                          "2×10 . If is even, set = 7×10 . Repeat: until = . As an example, let " \
                          "us find the rounded-square-root of = 4321. has 4 digits, so = 7×10 = " \
                          "70. Since = , we stop here. So, after just two iterations, we have " \
                          "found that the rounded-square-root of 4321 is 66 (the actual square " \
                          "root is 65.7343137…). The number of iterations required when using " \
                          "this method is surprisingly low. For example, we can find the " \
                          "rounded-square-root of a 5-digit integer (10,000 ≤ ≤ 99,999) with an " \
                          "average of 3.2102888889 iterations (the average value was rounded to " \
                          "10 decimal places). Using the procedure described above, what is the " \
                          "average number of iterations required to find the rounded-square-root " \
                          "of a 14-digit number (10 ≤ < 10 )? Give your answer rounded to 10 " \
                          "decimal places. Note: The symbols ⌊ ⌋ and ⌈ ⌉ represent the and " \
                          "respectively."

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

