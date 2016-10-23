# class Solution(object):
#     def partition(self, s):
#         """
#         :type s: str
#         :rtype: List[List[str]]
#         """
#         return self.partitions(s, 0, [])
#
#     def partitions(self, s, l, part):
#         if l == 0:
#             return self.partitions(s, l + 1, [s[l]])
#         if l == len(s):
#             pal = filter(Solution.is_pal, part)
#             if len(part) == len(pal):
#                 return [part]
#             else:
#                 return []
#         old_word = part[:-1] + [part[-1] + s[l]]
#         new_word = part + [s[l]]
#         return self.partitions(s, l + 1, old_word) + \
#                self.partitions(s, l + 1, new_word)
#
#     @staticmethod
#     def is_pal(s):
#         return s == s[::-1]
#
#
# if __name__ == "__main__":
#     print Solution().partition("aab")

#
# def partitions(s, l, part):
#     if l == 0:
#         return partitions(s, l + 1, [s[l]])
#     if l == len(s):
#         return [part]
#     old_word = part[:-1] + [part[-1] + s[l]]
#     new_word = part + [s[l]]
#     return partitions(s, l + 1, old_word) + partitions(s, l + 1, new_word)
#
#
# print partitions("abc", 0, [])


# class Solution(object):
#     def partition(self, s):
#         """
#         :type s: str
#         :rtype: List[List[str]]
#         """
#         result = []
#         parts = self.partitions(s, 0, [])
#         for part in parts:
#             pal = filter(Solution.is_pal, part)
#             if len(part) == len(pal):
#                 result.append(part)
#         return result
#
#     def partitions(self, s, l, part):
#         if l == 0:
#             return self.partitions(s, l + 1, [s[l]])
#         if l == len(s):
#             return [part]
#         old_word = part[:-1] + [part[-1] + s[l]]
#         new_word = part + [s[l]]
#         return self.partitions(s, l + 1, old_word) + \
#                self.partitions(s, l + 1, new_word)
#
#     @staticmethod
#     def is_pal(s):
#         return s == s[::-1]

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return self.partitions(s, 0, [])

    def partitions(self, s, k, current):
        acc = []
        if k is len(s):
            return [current]
        for i in range(k, len(s)):
            if Solution.is_pal(s[k:i + 1]):
                acc += self.partitions(s, i + 1, current + [s[k:i + 1]])
        return acc

    @staticmethod
    def is_pal(s):
        return s == s[::-1]


if __name__ == "__main__":
    print Solution().partition("aab")
