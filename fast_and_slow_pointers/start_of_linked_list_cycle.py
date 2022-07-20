class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def start_of_linked_list_cycle(head: Node) -> bool:
    """
    Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

    Time Complexity: O(n) where n = len(arr)
    Space Complexity: O(1)
    """
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            current = head

            while current is not slow:
                current = current.next
                slow = slow.next

            return slow

    return None


    

def test_start_of_linked_list_cycle():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(start_of_linked_list_cycle(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(start_of_linked_list_cycle(head).value))


if __name__ == "__main__":
    test_start_of_linked_list_cycle()
