
__problem_title__ = "Integer partition equations"
__problem_url___ = "https://projecteuler.net/problem=207"
__problem_description__ = "For some positive integers , there exists an integer partition of the " \
                          "form 4 = 2 + , where 4 , 2 , and are all positive integers and is a " \
                          "real number. The first two such partitions are 4 = 2 + 2 and 4 = 2 + " \
                          "6. Partitions where is also an integer are called . For any ≥ 1 let " \
                          "P( ) be the proportion of such partitions that are perfect with ≤ . " \
                          "Thus P(6) = 1/2. In the following table are listed some values of P( " \
                          ") P(5) = 1/1 P(10) = 1/2 P(15) = 2/3 P(20) = 1/2 P(25) = 1/2 P(30) = " \
                          "2/5 ... P(180) = 1/4 P(185) = 3/13 Find the smallest for which P( ) < " \
                          "1/12345"

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

