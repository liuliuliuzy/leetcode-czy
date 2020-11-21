#include "basicInclude.h"

class Solution {
public:
    ListNode* sortList(ListNode* head) {
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
};


class SolutionBetter {
    /*
    归并排序，其实将两个排好序的链表合并是容易做到的事，所以从顶向下归并排序，只需要确定start\end\mid指针即可
    而确定指针的方法就是，两个从头开始向后运动的指针，一个移动的速度是另一个的两倍(处理链表问题的一种思维方式)
    */
public:
    ListNode* sortList(ListNode* head) {
        return sortList(head, nullptr);
    }

    ListNode* sortList(ListNode* head, ListNode* tail) {
        if (head == nullptr) {
            return head;
        }
        if (head->next == tail) {
            head->next = nullptr;
            return head;
        }
        ListNode* slow = head, *fast = head;
        while (fast != tail) {
            slow = slow->next;
            fast = fast->next;
            if (fast != tail) {
                fast = fast->next;
            }
        }
        ListNode* mid = slow;
        return merge(sortList(head, mid), sortList(mid, tail));
    }

    ListNode* merge(ListNode* head1, ListNode* head2) {
        ListNode* dummyHead = new ListNode(0);
        ListNode* temp = dummyHead, *temp1 = head1, *temp2 = head2;
        while (temp1 != nullptr && temp2 != nullptr) {
            if (temp1->val <= temp2->val) {
                temp->next = temp1;
                temp1 = temp1->next;
            } else {
                temp->next = temp2;
                temp2 = temp2->next;
            }
            temp = temp->next;
        }
        if (temp1 != nullptr) {
            temp->next = temp1;
        } else if (temp2 != nullptr) {
            temp->next = temp2;
        }
        return dummyHead->next;
    }
};

int main()
{
    vector<int> nums;
    srand(time(0));
    int length = rand()%10+1;
    for(int i=0; i<length; i++){
        nums.push_back(rand()%10+1);
    }
    Solution s;
    ListNode* head = getLinkedList(nums);
    printLinkedList(head);
    printLinkedList(s.sortList(head));

    return 0;
}