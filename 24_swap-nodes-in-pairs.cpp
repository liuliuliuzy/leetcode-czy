/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <cstdlib>
#include <cstdio>

//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    
    void swapPairs(ListNode* head) {
        ListNode* tmp1 = head->next->next;
        ListNode* tmp2 = head;
        head = head->next;
        tmp2->next = tmp1;
        head->next = tmp2;
    }
    void printLinkedList(ListNode* head) {
        ListNode* tmp = head;
        while (tmp)
        {
            printf("val: %d\n", tmp->val);
            tmp = tmp->next;
        }
    }
};

int main()
{
    Solution so;
    ListNode s(1);
    ListNode s2(2);
    ListNode s3(3);
    ListNode s4(4);
    s.next = (ListNode*)(&s2);
    s2.next = (ListNode*)(&s3);
    s3.next = (ListNode*)(&s4);
    so.printLinkedList(&s);
    so.swapPairs(&s);
    so.printLinkedList(&s);
    return 0;
}