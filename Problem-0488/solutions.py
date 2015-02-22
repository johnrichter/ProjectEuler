
__problem_title__ = "Unbalanced Nim"
__problem_url___ = "https://projecteuler.net/problem=488"
__problem_description__ = "Alice and Bob have enjoyed playing every day. However, they finally " \
                          "got bored of playing ordinary three-heap Nim. So, they added an extra " \
                          "rule: - Must not make two heaps of the same size. The triple ( , , ) " \
                          "indicates the size of three heaps. Under this extra rule, (2,4,5) is " \
                          "one of the losing positions for the next player. To illustrate: - " \
                          "Alice moves to (2,4,3) - Bob moves to (0,4,3) - Alice moves to " \
                          "(0,2,3) - Bob moves to (0,2,1) Unlike ordinary three-heap Nim, " \
                          "(0,1,2) and its permutations are the end states of this game. For an " \
                          "integer , we define F( ) as the sum of + + for all the losing " \
                          "positions for the next player, with 0 a b c N. For example, F(8) = " \
                          "42, because there are 4 losing positions for the next player, " \
                          "(1,3,5), (1,4,6), (2,3,6) and (2,4,5). We can also verify that F(128) " \
                          "= 496062. Find the last 9 digits of F(10 )."

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

