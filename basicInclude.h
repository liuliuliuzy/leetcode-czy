#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};