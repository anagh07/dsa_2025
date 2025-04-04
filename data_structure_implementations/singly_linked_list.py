from typing import List, Optional

"""
Design a Singly Linked List class.

Your LinkedList class should support the following operations:
    - LinkedList() will initialize an empty linked list.
    - int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
    - void insertHead(int val) will insert a node with val at the head of the list.
    - void insertTail(int val) will insert a node with val at the tail of the list.
    - bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
    - int[] getValues() return an array of all the values in the linked list, ordered from head to tail.

Example 1:
Input:
["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]

Output:
[null, null, null, true, [0, 2]]

Example 2:
Input:
["insertHead", 1, "insertHead", 2, "get", 5]

Output:
[null, null, -1]

Note:
The index int i provided to get(int i) and remove(int i) is guaranteed to be greater than or equal to 0.
"""


class LinkedList:
    """
    head -> Node -> Node -> tail(Node) -> None
    """

    def __init__(self):
        self.head = ListNode()
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        # index out of bounds
        if index < 0 or index > self.size:
            return -1
        # iterate and find node
        curr = self.head.next
        for i in range(index):
            curr = curr.next if curr else None
        return -1 if not curr else curr.value

    def insertHead(self, val: int) -> None:
        newNode = ListNode(value=val)
        newNode.next = self.head.next
        self.head.next = newNode
        if self.size == 0:
            self.tail = newNode
        self.size += 1

    def insertTail(self, val: int) -> None:
        newNode = ListNode(value=val)
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def remove(self, index: int) -> bool:
        # index out of bounds
        if index < 0 or index >= self.size:
            return False
        # remove head
        if index == 0:
            first = self.head.next
            if first and not first.next:
                # length 1: head -> tail(node)
                # update tail
                self.head.next = None
                self.tail = self.head
                self.size -= 1
                return True
            elif first and first.next:
                # length 2/3/4...: head -> node -> node -> tail(node)
                self.head.next = first.next
                self.size -= 1
                return True

        # iterate to previous element before target
        curr = self.head
        for i in range(index):
            curr = curr.next if curr else None
        # remove operation
        if curr:
            curr.next = curr.next.next if curr.next else None

        # tail remove check
        if index == self.size - 1:
            self.tail = curr

        # adjust size
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        values: List[int] = []
        current_node = self.head.next
        while current_node is not None:
            if current_node.value is not None:
                values.append(current_node.value)
            current_node = current_node.next
        return values


class ListNode:
    def __init__(self, value=-1, next=None):
        self.value = value
        self.next: Optional["ListNode"] = next


def main():
    # ["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]
    test_case_2 = LinkedList()
    test_case_2.insertHead(1)
    test_case_2.insertTail(2)
    test_case_2.insertHead(0)
    print(test_case_2.getValues())
    print(test_case_2.remove(1))
    print(test_case_2.getValues())

    # ["insertTail", 1, "insertTail", 2, "get", 1, "remove", 1, "insertTail", 2, "get", 1, "get", 0]
    print("\n***********")
    print("Test Case 1")
    test_case_1 = LinkedList()
    test_case_1.insertTail(1)
    test_case_1.insertTail(2)
    print(test_case_1.get(1))  # 2
    print(test_case_1.remove(1))  # True
    test_case_1.insertTail(2)
    print(test_case_1.get(1))  # 2
    print(test_case_1.get(0))  # 1


if __name__ == "__main__":
    main()
