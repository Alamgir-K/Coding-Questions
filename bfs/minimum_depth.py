from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def minimum_depth(root: TreeNode) -> list:
    """
    Find the minimum depth of a binary tree. 
    The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.

    Time Complexity: O(n) where n = len(arr)
    Space Complexity: O(n)
    """
    if root is None:
        return -1

    queue = deque()
    queue.append(root)
    depth = 0

    while queue:
        level_size = len(queue)
        depth += 1

        for _ in range(0, level_size):
            current = queue.popleft()
            
            if current.left is None and current.right is None:
                return depth

            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)
    
    return depth 


def maximum_depth(root: TreeNode):
    """
    Find the maximum depth of a binary tree. 

    Time Complexity: O(n) where n = len(arr)
    Space Complexity: O(n)
    """
    if root is None:
        return -1

    queue = deque()
    queue.append(root)
    depth = 0

    while queue:
        depth += 1
        level_size = len(queue)

        for _ in range(0, level_size):
            current = queue.popleft()

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)
        
    return depth





def test_minimum_depth():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(minimum_depth(root)))
    print("Tree Maximum Depth: " + str(maximum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(minimum_depth(root)))
    print("Tree Maximum Depth: " + str(maximum_depth(root)))


if __name__ == "__main__":
    test_minimum_depth()
