#Recursive solution to the 0/1 Knapsack Problem
def knapsack(val,wt,W,n):
    if n==0 or W==0:
        return 0
    accept = 0
    if(wt[n-1]<=W):
        accept = val[n-1]+knapsack(val,wt,W-wt[n-1],n-1)
    reject = knapsack(val,wt,W,n-1)
    return (max(accept,reject))


val = [100,72,46]
wt = [4,3,2]
W = 5
n = len(val)
print(knapsack(val,wt,W,n))