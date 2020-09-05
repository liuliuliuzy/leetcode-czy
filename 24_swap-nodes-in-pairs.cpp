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
    void swapHelper(ListNode*& head){
        ListNode* tmp1 = head->next->next;
        ListNode* tmp2 = head;
        head = head->next;
        tmp2->next = tmp1;
        head->next = tmp2;
    }
    //错误尝试
    ListNode* swapPairsV2(ListNode* head) {
        ListNode* ans;
        bool flag = true;
        while (head && head->next)
        {
            printf("%s %d\n", "1", head->val);
            swapHelper(head);
            printf("%s %d %d\n", "21", head->val, head->next->val);
            if(flag){
                ans = head;
                flag = false;
            }
            head = head->next->next;
            if(head){
                printf("%s %d\n", "213", head->val);
            }  
        }
        return ans;
    }
    ListNode* swapPairs(ListNode* head){
        //终止条件
        if(!head || !head->next){
            return head;
        }
        ListNode* t1 = head;
        ListNode* t2 = head->next->next;
        head = head->next;
        head->next = t1;
        t1->next = swapPairs(t2);
        return head;
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
    ListNode s5(5);
    ListNode s6(6);
    s.next = (ListNode*)(&s2);
    s2.next = (ListNode*)(&s3);
    s3.next = (ListNode*)(&s4);
    s4.next = (ListNode*)(&s5);
    s5.next = (ListNode*)(&s6);
    so.printLinkedList(&s);
    so.printLinkedList(so.swapPairs(&s));
    // so.printLinkedList(head);
    return 0;
}