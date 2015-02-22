
__problem_title__ = "Product-sum numbers"
__problem_url___ = "https://projecteuler.net/problem=88"
__problem_description__ = "A natural number, N, that can be written as the sum and product of a " \
                          "given set of at least two natural numbers, { , , ... , } is called a " \
                          "product-sum number: N = + + ... + = × × ... × . For example, 6 = 1 + " \
                          "2 + 3 = 1 × 2 × 3. For a given set of size, , we shall call the " \
                          "smallest N with this property a minimal product-sum number. The " \
                          "minimal product-sum numbers for sets of size, = 2, 3, 4, 5, and 6 are " \
                          "as follows. =2: 4 = 2 × 2 = 2 + 2 =3: 6 = 1 × 2 × 3 = 1 + 2 + 3 =4: 8 " \
                          "= 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4 =5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 " \
                          "+ 2 + 2 =6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6 Hence " \
                          "for 2≤ ≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 " \
                          "= 30; note that 8 is only counted once in the sum. In fact, as the " \
                          "complete set of minimal product-sum numbers for 2≤ ≤12 is {4, 6, 8, " \
                          "12, 15, 16}, the sum is 61. What is the sum of all the minimal " \
                          "product-sum numbers for 2≤ ≤12000?"

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

