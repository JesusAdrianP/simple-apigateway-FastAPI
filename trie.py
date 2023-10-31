from typing import Optional


class Trie:
    def __init__(self):
        self.root = self.Node()

    def insert(self, s: str) -> None:
        node = self.root
        for ch in s:
            if ch not in node.children:
                node.children[ch] = self.Node()
            node = node.children[ch]
        node.is_end = True

    def search(self, s: str) -> Optional['Trie.Node']:
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node if node.is_end else None
    

    def get_strings(self):
        def rec(node: 'Trie.Node', string: list[str], all_strings: list[str]) -> list[str]:
            if node.is_end:
                all_strings.append("".join(string))

            for ch in node.children:
                string.append(ch)
                rec(node.children[ch], string, all_strings)
                string.pop()

        all_strings = []
        rec(self.root, [], all_strings)

        return all_strings
    


    class Node:
        def __init__(self, is_end=False):
            self.children = {}
            self.is_end = is_end
    