
__problem_title__ = "An amazing Prime-generating Automaton"
__problem_url___ = "https://projecteuler.net/problem=308"
__problem_description__ = "A program written in the programming language Fractran consists of a " \
                          "list of fractions. The internal state of the Fractran Virtual Machine " \
                          "is a positive integer, which is initially set to a seed value. Each " \
                          "iteration of a Fractran program multiplies the state integer by the " \
                          "first fraction in the list which will leave it an integer. For " \
                          "example, one of the Fractran programs that John Horton Conway wrote " \
                          "for prime-generation consists of the following 14 fractions: Starting " \
                          "with the seed integer 2, successive iterations of the program produce " \
                          "the sequence: 15, 825, 725, 1925, 2275, 425, ..., 68, , 30, ..., 136, " \
                          ", 60, ..., 544, , 240, ... The powers of 2 that appear in this " \
                          "sequence are 2 , 2 , 2 , ... It can be shown that the powers of 2 in " \
                          "this sequence have prime exponents and that the primes appear as " \
                          "exponents of powers of 2, in proper order! If someone uses the above " \
                          "Fractran program to solve Project Euler Problem 7 (find the 10001 " \
                          "prime), how many iterations would be needed until the program " \
                          "produces 2 ?"

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

