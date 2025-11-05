from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 if list1 else list2
        return dummy.next
    
list1 = [1,2,4]
list2 = [1,3,4]
example = Solution()
result1 = example.mergeTwoLists(list1, list2)
print(result1)

list1 = []
list2 = []
result2 = example.mergeTwoLists(list1, list2)
print(result2)

list1 = []
list2 = [0]
result3 = example.mergeTwoLists(list1, list2)
print(result3)
        