/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    ListNode* insertionSortList(ListNode* head) {
        // 如果链表为空或者只有一个元素
        if(! head || ! (head->next)){
            return head;
        }

        ListNode* tail = head;
        ListNode* node = tail->next;
        tail->next = NULL;

        while (node)
        {
            // printLinkedList(head);
            // 如果节点不比尾部节点值小
            if(tail->val <= node->val){
                tail->next = node;
                tail = tail->next;
                node = tail->next;
                tail->next = NULL;
                continue;
            }
            // 从第一个节点开始比较
            ListNode* tmp = head;
            // 如果插入到头部
            if(tmp->val > node->val){
                tail->next = node->next;
                node->next = tmp;
                head = node;
                node = tail->next;
                continue;
            }
            // 插入到中间
            while (tmp->next && tmp->next->val <= node->val)
            {
                tmp = tmp->next;
            }

            tail->next = node->next;
            node->next = tmp->next;
            tmp->next = node;
            node = tail->next;
            tail->next = NULL;
        }
        
        return head;
    }
    ListNode* insertOne(ListNode* head){
        return NULL;
    }
    void printLinkedList(ListNode* head){
        ListNode* tmp = head;
        while (tmp)
        {
            cout<<tmp->val<<", ";
            tmp = tmp->next;
        }
        cout<<endl;
    }
};

int main()
{
    Solution s;

    vector<int> nums = {2,1,3};
    // srand(time(0));
    // for(int i=0; i < 10; i++){
    //     nums.push_back(rand()%20+1);
    // }
    ListNode* head = s.getLinkedList(nums);
    // ListNode oneNode(2);
    // ListNode* node = &oneNode;
    s.printLinkedList(head);
    // ListNode* tmp = head;
    
    head = s.insertionSortList(head);
    s.printLinkedList(head);

    return 0;
}