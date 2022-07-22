class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def all_sum_paths(root: TreeNode, S: int) -> list:
    """
    Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

    Time Complexity: O(nlogn) where n = len(arr)
    Space Complexity: O(nlogn)
    """
    def find_paths(current, target, current_path, all_paths):
        if not current:
            return

        current_path.append(current.val)

        if current.val == target and current.left is None and current.right is None:
            all_paths.append(list(current_path))
        else:
            find_paths(current.left, target - current.val, current_path, all_paths)
            find_paths(current.right, target - current.val, current_path, all_paths)

        current_path.pop()


    paths = []
    find_paths(root, S, [], paths)

    return paths    
    

def test_all_sum_paths():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
            ": " + str(all_sum_paths(root, sum)))


if __name__ == "__main__":
    test_all_sum_paths()
