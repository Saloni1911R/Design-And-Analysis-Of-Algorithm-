def merging(A,B):
    merge = [0]*(len(A)+len(B))
    i,j,k = 0,0,0
    while (i<len(A) and j < len(B)):
        if(A[i] < B[j]):
            merge[k] = A[i]
            i = i+1
            k = k+1
        else :
            merge[k] = B[j]
            j = j+1
            k = k+1
    while(i<len(A)):
        merge[k] = A[i]
        i = i+1
        k = k+1
    while(j<len(B)):
        merge[k] = B[j]
        j = j+1
        k = k+1
    return merge

A = [1,3,4,5,6,7,9,15]
B = [2,8,16,19,56]

print(merging(A,B))