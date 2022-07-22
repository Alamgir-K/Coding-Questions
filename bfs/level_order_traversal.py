from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def level_order_traversal(root: TreeNode) -> bool:
    """
    Given a binary tree, populate an array to represent its level-by-level traversal. 
    You should populate the values of all nodes of each level from left to right in separate sub-arrays.

    Time Complexity: O(n) where n = len(arr)
    Space Complexity: O(n)
    """
    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(0, level_size):
            current = queue.popleft()
            current_level.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        result.append(current_level)
    
    return result
    

def test_level_order_traversal():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(level_order_traversal(root)))


if __name__ == "__main__":
    test_level_order_traversal()
