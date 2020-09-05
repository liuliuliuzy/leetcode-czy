def maxScoreSightseeingPair(A)->int:
    if len(A)==2:
        return A[0]+A[1]-1
    tmp = A[0]
    bestScore = 0
    #从前往后遍历j
    for j in range(1, len(A)):
        if tmp+A[j]-j > bestScore:
            bestScore = tmp+A[j]-j
        if A[j]+j > tmp:
            tmp = A[j]+j
    return bestScore

if __name__ == "__main__":
    A = [3, 7, 2, 3]
    print(maxScoreSightseeingPair(A))