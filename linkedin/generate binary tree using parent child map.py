'''
Given a list of child->parent relationships, build a binary tree out of it. All the element Ids inside the tree are unique.

Example:

Given the following relationships:

Child Parent IsLeft
15 20 true
19 80 true
17 20 false
16 80 false
80 50 false
50 null false
20 50 true

You should return the following tree:

    50
   /  \
  20   80
 / \   / \
15 17 19 16
'''
from collections import defaultdict
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, lst):
        if not lst:
            return None
        # Initialize a queue
        q = []
        # Create a map of parent to list of children with direction
        parents = defaultdict(list)
        for item in lst:
            child, parent, isLeft = item
            if parent == None:
                q = [Node(child)]
            else:
                parents[parent].append((child, isLeft))

        head = q[0]
        while q:
            node = q.pop()
            children = parents[node.val]
            if not children:
                continue
            left = children[0] if children[0][1] == True else children[1]
            right = children[0] if children[0][1] == False else children[1]
            left_node = Node(left[0])
            right_node = Node(right[0])
            node.left = left_node
            node.right = right_node
            q.append(left_node)
            q.append(right_node)
        return head

    def printTreeLevelOrder(self, head):
        if not head:
            return
        q = [head]
        res = []
        while q:
            next_level = []
            while q:
                node = q.pop(0)
                next_level.append(node)
            res.append([x.val for x in next_level])
            for node in next_level:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res

lst = [[15,20,True], [19,80,True], [17,20,False], [16,80,False], [80,50,False], [50,None,False],[20,50,True]]
head = Solution().buildTree(lst)
print(Solution().printTreeLevelOrder(head))
