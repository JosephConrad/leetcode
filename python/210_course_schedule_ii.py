class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[y].append(x)
        return self.topologicSort(numCourses, graph)

    def topologicSort(self, numCourses, graph):
        stack = []
        visited = [0] * numCourses
        for i in range(numCourses):
            if visited[i] != 1:
                if self.topologicSortHelper(i, stack, graph, visited):
                    return []
        return stack[::-1]

    def topologicSortHelper(self, i, stack, graph, visited):

        # isCycle
        if visited[i] == -1:
            return True

        visited[i] = -1
        for neighbour in graph[i]:
            if visited[neighbour] != 1:
                if self.topologicSortHelper(neighbour, stack, graph, visited):
                    return True

        visited[i] = 1
        stack.append(i)
        return False


if __name__ == "__main__":
    print Solution().findOrder(2, [[1, 0]])
    print Solution().findOrder(2, [[0, 1], [1, 0]])
    print Solution().findOrder(2, [[0, 1]])
    print Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
