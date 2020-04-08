'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            #print(head.val)
            stack.append(head.val)
            head = head.next
        ret = []
        #i = len(stack)
        while stack:
            ret.append(stack.pop())
        return ret
'''
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        def recursive(node):
            if node.next:
                later = recursive(node.next)
                return later + [node.val]
            else:
                return [node.val]
        if head:
            return (recursive(head))
        else:
            return []
'''


# 探索递归与迭代的关系
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        
        

