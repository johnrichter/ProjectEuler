
__problem_title__ = "Repeated permutation"
__problem_url___ = "https://projecteuler.net/problem=483"
__problem_description__ = "We define a as an operation that rearranges the order of the elements " \
                          "{1, 2, 3, ..., n}. There are n! such permutations, one of which " \
                          "leaves the elements in their initial order. For n = 3 we have 3! = 6 " \
                          "permutations: - P = keep the initial order - P = exchange the 1 and 2 " \
                          "elements - P = exchange the 1 and 3 elements - P = exchange the 2 and " \
                          "3 elements - P = rotate the elements to the right - P = rotate the " \
                          "elements to the left If we select one of these permutations, and we " \
                          "re-apply the permutation repeatedly, we eventually restore the " \
                          "initial order. For a permutation P , let f(P ) be the number of steps " \
                          "required to restore the initial order by applying the permutation P " \
                          "repeatedly. For n = 3, we obtain: - f(P ) = 1 : (1,2,3) → (1,2,3) - " \
                          "f(P ) = 2 : (1,2,3) → (2,1,3) → (1,2,3) - f(P ) = 2 : (1,2,3) → " \
                          "(3,2,1) → (1,2,3) - f(P ) = 2 : (1,2,3) → (1,3,2) → (1,2,3) - f(P ) = " \
                          "3 : (1,2,3) → (3,1,2) → (2,3,1) → (1,2,3) - f(P ) = 3 : (1,2,3) → " \
                          "(2,3,1) → (3,1,2) → (1,2,3) Let g(n) be the average value of f (P ) " \
                          "over all permutations P of length n. g(3) = (1 + 2 + 2 + 2 + 3 + 3 " \
                          ")/3! = 31/6 ≈ 5.166666667e0 g(5) = 2081/120 ≈ 1.734166667e1 g(20) = " \
                          "12422728886023769167301/2432902008176640000 ≈ 5.106136147e3 Find " \
                          "g(350) and write the answer in scientific notation rounded to 10 " \
                          "significant digits, using a lowercase e to separate mantissa and " \
                          "exponent, as in the examples above."

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

