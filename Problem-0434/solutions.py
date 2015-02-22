
__problem_title__ = "Rigid graphs"
__problem_url___ = "https://projecteuler.net/problem=434"
__problem_description__ = "Recall that a graph is a collection of vertices and edges connecting " \
                          "the vertices, and that two vertices connected by an edge are called " \
                          "adjacent. Graphs can be embedded in Euclidean space by associating " \
                          "each vertex with a point in the Euclidean space. A graph is an " \
                          "embedding of a graph where it is possible to move one or more " \
                          "vertices continuously so that the distance between at least two " \
                          "nonadjacent vertices is altered while the distances between each pair " \
                          "of adjacent vertices is kept constant. A graph is an embedding of a " \
                          "graph which is not flexible. Informally, a graph is rigid if by " \
                          "replacing the vertices with fully rotating hinges and the edges with " \
                          "rods that are unbending and inelastic, no parts of the graph can be " \
                          "moved independently from the rest of the graph. The embedded in the " \
                          "Euclidean plane are not rigid, as the following animation " \
                          "demonstrates: However, one can make them rigid by adding diagonal " \
                          "edges to the cells. For example, for the 2x3 grid graph, there are 19 " \
                          "ways to make the graph rigid: Note that for the purposes of this " \
                          "problem, we do not consider changing the orientation of a diagonal " \
                          "edge or adding both diagonal edges to a cell as a different way of " \
                          "making a grid graph rigid. Let ( , ) be the number of ways to make " \
                          "the × grid graph rigid. E.g. (2,3) = 19 and (5,5) = 23679901 Define ( " \
                          ") as ∑ ( , ) for 1 ≤ , ≤ . E.g. (5) = 25021721. Find (100), give your " \
                          "answer modulo 1000000033"

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

