# Definition for a binary tree node.
from collections import defaultdict


# based on:
# https://discuss.leetcode.com/topic/41687/compact-python-solution
class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.isWord = True

    def search(self, word, isWord=True):
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.isWord if isWord else True

    def startsWith(self, prefix):
        return self.search(prefix, False)


if __name__ == "__main__":
    obj = Trie()
    obj.insert("ala")
    param_2 = obj.search("ala")
    print param_2
    param_3 = obj.startsWith("a")
    print param_3
    param_4 = obj.startsWith("b")
    print param_4
