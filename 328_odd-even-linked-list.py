# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: 'int'=0, next: 'ListNode'=None):
        self.val = val
        self.next = next

    def printSelf(self):
        tmp = self
        while tmp != None:
            print(tmp.val, end=" ")
            tmp = tmp.next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        '''
        调整链表
        注意链表数据结构的特殊性
        '''
        oddTmp = head
        evenNode = evenTmp = None
        if head.next:
            evenNode = evenTmp = head.next
        # while oddTmp != None and oddTmp.next != None and oddTmp.next.next != None:
        #     # if oddTmp:
        #     # if oddTmp.next and oddTmp.next.next:
        #     oddTmp.next =  oddTmp.next.next
        #     oddTmp = oddTmp.next
        # while evenTmp != None and evenTmp.next != None and evenTmp.next.next != None:
        #     # if evenTmp.next and evenTmp.next.next:
        #     evenTmp.next = evenTmp.next.next
        #     evenTmp = evenTmp.next
        while (oddTmp and oddTmp.next and oddTmp.next.next) or (evenTmp and evenTmp.next and evenTmp.next.next):
            if oddTmp.next and oddTmp.next.next:
                oddTmp.next =  oddTmp.next.next
                oddTmp = oddTmp.next           
            if evenTmp.next and evenTmp.next.next:
                evenTmp.next = evenTmp.next.next
                evenTmp = evenTmp.next
        oddTmp.next = evenNode
            


if __name__ == "__main__":
    a5 = ListNode(5)
    a4 = ListNode(4, a5)
    a3 = ListNode(3, a4)
    a2 = ListNode(2, a3)
    a1 = ListNode(1, a2)
    a1.printSelf()
    s = Solution()
    s.oddEvenList(a1)
    a1.printSelf()