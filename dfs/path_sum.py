class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def sum_path(root: TreeNode, S: int) -> bool:
    """
    Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.

    Time Complexity: O(n) where n = len(arr)
    Space Complexity: O(n)
    """
    if not root:
        return None

    if root.val == S and root.left is None and root.right is None:
        return True

    return sum_path(root.left, S - root.val) or sum_path(root.right, S - root.val)
    

def test_sum_path():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(sum_path(root, 23)))
    print("Tree has path: " + str(sum_path(root, 16)))


if __name__ == "__main__":
    test_sum_path()
