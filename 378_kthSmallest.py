from typing import List

def kthSmallest(matrix: List[List[int]], k: int) -> int:
    return 1

def mergeSort(A: List[int], B: List[int]) -> List[int]:
    res = []
    #make sure that A and B are not empty
    Aindex = Bindex = 0
    while Aindex < len(A) and Bindex < len(B):
        if A[Aindex] < B[Bindex]:
            res.append(A[Aindex])
            Aindex += 1
        else:
            res.append(B[Bindex])
            Bindex += 1
    if Aindex == len(A):
        res += B[Bindex:]
    else:
        res += A[Aindex:]
    return res


if __name__ == "__main__":
    a = [2, 3, 6]
    b = [1, 4, 7, 9]
    print(mergeSort(a, b))