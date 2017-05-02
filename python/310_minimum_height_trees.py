class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        adj = [set() for _ in range(n)]
        for v1, v2 in edges:
            adj[v1].add(v2)
            adj[v2].add(v1)

        leaves = [i for i in xrange(n) if len(adj[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for l in leaves:
                v = adj[l].pop()
                adj[v].remove(l)
                if len(adj[v]) == 1:
                    new_leaves.append(v)
            leaves = new_leaves
        return leaves


if __name__ == "__main__":
    print Solution().findMinHeightTrees(n=6, edges=[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
