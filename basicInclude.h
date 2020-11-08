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

//使用标准命名空间
using namespace std;

//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};