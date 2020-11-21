//标准库
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <iostream>
#include <cmath>
//常用的标准容器-数据结构
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <unordered_set>

#include <ctime>
//使用标准命名空间
using namespace std;

//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

//打印链表
void printLinkedList(ListNode* head) {
    ListNode* tmp = head;
    while (tmp)
    {
        printf("val: %d\n", tmp->val);
        tmp = tmp->next;
    }
}

//向量转链表
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