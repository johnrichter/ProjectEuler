
__problem_title__ = "Permutation of 3-smooth numbers"
__problem_url___ = "https://projecteuler.net/problem=462"
__problem_description__ = "A is an integer which has no prime factor larger than 3. For an " \
                          "integer , we define S( ) as the set of 3-smooth numbers less than or " \
                          "equal to . For example, S(20) = { 1, 2, 3, 4, 6, 8, 9, 12, 16, 18 }. " \
                          "We define F( ) as the number of permutations of S( ) in which each " \
                          "element comes after all of its proper divisors. This is one of the " \
                          "possible permutations for = 20. - 1, 2, 4, 3, 9, 8, 16, 6, 18, 12. " \
                          "This is not a valid permutation because 12 comes before its divisor " \
                          "6. - 1, 2, 4, 3, 9, 8, , 16, , 18. We can verify that F(6) = 5, F(8) " \
                          "= 9, F(20) = 450 and F(1000) ≈ 8.8521816557e21. Find F(10 ). Give as " \
                          "your answer its scientific notation rounded to ten digits after the " \
                          "decimal point. When giving your answer, use a lowercase e to separate " \
                          "mantissa and exponent. E.g. if the answer is 112,233,445,566,778,899 " \
                          "then the answer format would be 1.1223344557e17."

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

