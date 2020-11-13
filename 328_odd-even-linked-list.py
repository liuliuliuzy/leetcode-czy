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
        if not head or not head.next:
            return head
        oddTmp = head
        evenNode = evenTmp = head.next
        while (oddTmp.next) or (evenTmp.next):
            if oddTmp.next and oddTmp.next.next:
                oddTmp.next =  oddTmp.next.next
                oddTmp = oddTmp.next
            else:
                break        
            if evenTmp.next and evenTmp.next.next:
                evenTmp.next = evenTmp.next.next
                evenTmp = evenTmp.next
            else:
                evenTmp.next = None
        oddTmp.next = evenNode      
        return head

if __name__ == "__main__":
    # a5 = ListNode(5)
    # a4 = ListNode(4)
    a3 = ListNode(3)
    a2 = ListNode(2, a3)
    a1 = ListNode(1, a2)
    a1.printSelf()
    print("")
    s = Solution()
    s.oddEvenList(a1)
    a1.printSelf()