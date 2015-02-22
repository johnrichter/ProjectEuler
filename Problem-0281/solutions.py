
__problem_title__ = "Pizza Toppings"
__problem_url___ = "https://projecteuler.net/problem=281"
__problem_description__ = "You are given a pizza (perfect circle) that has been cut into · equal " \
                          "pieces and you want to have exactly one topping on each slice. Let ( " \
                          ", ) denote the number of ways you can have toppings on the pizza with " \
                          "different toppings ( ≥ 2), using each topping on exactly slices ( ≥ " \
                          "1). Reflections are considered distinct, rotations are not. Thus, for " \
                          "instance, (2,1) = 1, (2,2) = (3,1) = 2 and (3,2) = 16. (3,2) is shown " \
                          "below: Find the sum of all ( , ) such that ( , ) ≤ 10 ."

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

