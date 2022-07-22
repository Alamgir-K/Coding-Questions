from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def zig_zag_traversal(root: TreeNode) -> list:
    """
    Given a binary tree, populate an array to represent its zigzag level order traversal. 
    You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.

    Time Complexity: O(n) where n = len(arr)
    Space Complexity: O(n)
    """
    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)
    left_to_right = True

    while queue:
        current_level = deque()
        level_size = len(queue)

        for _ in range(0, level_size):
            print(left_to_right)
            current = queue.popleft()

            if left_to_right:
                current_level.append(current.val)
            else:
                current_level.appendleft(current.val)

            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)
        
        left_to_right = not left_to_right
        result.append(list(current_level))

    return result
    

def test_zig_zag_traversal():
  
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(zig_zag_traversal(root)))


if __name__ == "__main__":
    test_zig_zag_traversal()
