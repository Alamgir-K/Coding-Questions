class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def linked_link_cycle(head: Node) -> bool:
    """
    Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

    Time Complexity: O(n) where n = len(arr)
    Space Complexity: O(1)
    """
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True
    
    return False
    

def test_linked_link_cycle():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    assert linked_link_cycle(head) == False

    head.next.next.next.next.next.next = head.next.next
    assert linked_link_cycle(head) == True

    head.next.next.next.next.next.next = head.next.next.next
    assert linked_link_cycle(head) == True


if __name__ == "__main__":
    test_linked_link_cycle()
