class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda (h, k): (-h, k))
        q = []
        for person in people:
            q.insert(person[1], person)
        return q


if __name__ == "__main__":
    print Solution().reconstructQueue(people=[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
