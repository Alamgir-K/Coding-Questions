class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def sum_path_nums(root: TreeNode) -> int:
    """
    Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

    Time Complexity: O(nlogn) where n = len(arr)
    Space Complexity: O(nlogn)
    """
    def find_nums(current, sum):
        if not current:
            return 0

        sum = (sum * 10) + current.val

        if current.left is None and current.right is None:
            return sum

        return find_nums(current.left, sum) + find_nums(current.right, sum)

    return find_nums(root, 0)
 
    

def test_sum_path_nums():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(sum_path_nums(root)))


if __name__ == "__main__":
    test_sum_path_nums()
