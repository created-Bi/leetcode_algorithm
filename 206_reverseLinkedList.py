# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 定义前驱结点
        p = None
        # 定义当前的结点
        c = head
        # 遍历当前结点，如果当前结点不为None
        while c:
            # 保存将当前结点的后继结点 
            a = c.next
            # 将当前结点的下一个结点 变为 前驱节点
            c.next = p
            # 将前驱节点 变为 当前结点
            p = c
            # 将当前结点 变为 原始后继结点
            c = a

        return p
