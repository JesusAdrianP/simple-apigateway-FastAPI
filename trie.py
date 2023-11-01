from typing import Optional


class Trie:
    """ Class to represent a Trie data structure"""

    def __init__(self):
        self.root = self.Node()

    def insert(self, s: str) -> None:
        """ inserst a new string to the trie """
        node = self.root
        for ch in s:
            if ch not in node.children:
                node.children[ch] = self.Node()
            node = node.children[ch]
        node.is_end = True

    def search(self, s: str) -> Optional['Trie.Node']:
        """ 
        Finds if the input string is part of the Trie, if its part of the Trie
        returns the trie node that contains the last elemet of the provided input string. 
        
        Otherwise returns None
        """
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node if node.is_end else None
    

    def get_strings(self) -> list[str]:
        """ Returns a list containing all the strings that are part of the trie """

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
    

    def longest_matched_string(self, s: str) -> Optional[str]:
        """
        Find the longest matching string in the Trie for the input string.

        example: 
            Lets say the Trie has this strings
                '/users' and '/users/api'

            if the input of the method is 
                '/users/api/token'
            Then the return value will be 
                '/users/api'

        """

        node = self.root
        longest_match = None
        matched_string = ""

        for ch in s:
            if ch not in node.children:
                break
            node = node.children[ch]
            matched_string += ch
            if node.is_end:
                longest_match = matched_string

        return longest_match
    


    class Node:
        """ Node class for the Trie data structure """
        def __init__(self, is_end=False):
            self.children = {}
            self.is_end = is_end
    
