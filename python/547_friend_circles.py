class Solution(object):
    def __init__(self):
        self.visited = set()

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(M)):
            if i not in self.visited:
                self.dfs(i, M)
                result += 1
        return result

    def dfs(self, node, M):
        for neighbour, friend in enumerate(M[node]):
            if friend and neighbour not in self.visited:
                self.visited.add(neighbour)
                self.dfs(neighbour, M)


if __name__ == "__main__":
    print Solution().findCircleNum([[1, 1, 0],
                                    [1, 1, 0],
                                    [0, 0, 1]])
