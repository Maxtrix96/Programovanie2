# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self, root) -> None:
        self.root = root

    def invertTree(self, root):
        if self.root:
            self.length = len(root)
            self.search_length = 0
            self.depth = 0
            while self.search_length < self.length: #find the depth of the tree
                self.search_length += 2**self.depth
                self.depth += 1 
            self.depth = self.depth

            self.inverted_tree = [self.root[0]]
            self.current_index = 0
            for i in range(self.depth): # create inverted tree by [::-1]ing the relevant segments of the tree
                self.current_index += 2**i
                self.inverted_tree.extend(self.root[self.current_index : self.current_index + 2**(i+1)][::-1])
            
            return self.inverted_tree
        else: return []



"""test = Solution([2,1,3])
test_parameters = test.invertTree(test.root)
print(f"Found length: {test.search_length}, Found depth: {test.depth}")
print(f"Inverted tree: {test.inverted_tree}")"""