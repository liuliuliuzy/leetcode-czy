#include "basicInclude.h"

class Solution {
public:
    ListNode* getLinkedList(vector<int>& nums)
    {
        ListNode* head = new ListNode(nums[0]);
        ListNode* tmp = head;
        for(int i=1; i<nums.size(); i++){
            tmp->next = new ListNode(nums[i]);
            tmp = tmp->next;
        }
        return head;
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int length = 0;
        ListNode* tmp = head;
        while (tmp)
        {
            length++;
            tmp = tmp->next;
        }
        if(n == length){
            return head->next;
        }
        int count = 0;
        tmp = head;
        while (count < length-n-1)
        {
            count++;
            tmp = tmp->next;
        }
        ListNode* t2 = tmp->next;
        tmp->next = t2->next;
        t2->next = NULL;
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
    vector<int> testnumbers = {2, 4, 5, 7, 9};
    Solution s;
    ListNode* head = s.getLinkedList(testnumbers);
    s.printLinkedList(head);
    s.printLinkedList(s.removeNthFromEnd(head, 3));
    return 0;
}