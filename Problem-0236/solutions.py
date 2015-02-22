
__problem_title__ = "Luxury Hampers"
__problem_url___ = "https://projecteuler.net/problem=236"
__problem_description__ = "Suppliers 'A' and 'B' provided the following numbers of products for " \
                          "the luxury hamper market: Although the suppliers try very hard to " \
                          "ship their goods in perfect condition, there is inevitably some " \
                          "spoilage - products gone bad. The suppliers compare their performance " \
                          "using two types of statistic: To their surprise, the suppliers found " \
                          "that each of the five per-product spoilage rates was worse (higher) " \
                          "for 'B' than for 'A' by the same factor (ratio of spoilage rates), " \
                          ">1; and yet, paradoxically, the overall spoilage rate was worse for " \
                          "'A' than for 'B', also by a factor of . There are thirty-five >1 for " \
                          "which this surprising result could have occurred, the smallest of " \
                          "which is 1476/1475. What's the largest possible value of ? Give your " \
                          "answer as a fraction reduced to its lowest terms, in the form / ."

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

