class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph, visited = [[]] * numCourses, [0] * numCourses
        for x, y in prerequisites:
            graph[x].append(y)
        return all(not self.isCycle(i, visited, graph) for i in range(numCourses))

    def isCycle(self, i, visited, graph):
        if visited[i] == -1:
            return True
        if visited[i] == 1:
            return False
        visited[i] = -1
        for neighbour in graph[i]:
            if self.isCycle(neighbour, visited, graph):
                return True
        visited[i] = 1
        return False


if __name__ == "__main__":
    print Solution().canFinish(1, [])
