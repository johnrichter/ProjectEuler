
__problem_title__ = "2011 nines"
__problem_url___ = "https://projecteuler.net/problem=318"
__problem_description__ = "Consider the real number √2+√3. When we calculate the even powers of " \
                          "√2+√3 we get: (√2+√3) = 9.898979485566356... (√2+√3) = " \
                          "97.98979485566356... (√2+√3) = 969.998969071069263... (√2+√3) = " \
                          "9601.99989585502907... (√2+√3) = 95049.999989479221... (√2+√3) = " \
                          "940897.9999989371855... (√2+√3) = 9313929.99999989263... (√2+√3) = " \
                          "92198401.99999998915... It looks like that the number of consecutive " \
                          "nines at the beginning of the fractional part of these powers is " \
                          "non-decreasing. In fact it can be proven that the fractional part of " \
                          "(√2+√3) approaches 1 for large n. Consider all real numbers of the " \
                          "form √p+√q with p and q positive integers and p<q, such that the " \
                          "fractional part of (√p+√q) approaches 1 for large n. Let C(p,q,n) be " \
                          "the number of consecutive nines at the beginning of the fractional " \
                          "part of (√p+√q) . Let N(p,q) be the minimal value of n such that " \
                          "C(p,q,n) ≥ 2011. Find ∑N(p,q) for p+q ≤ 2011."

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

