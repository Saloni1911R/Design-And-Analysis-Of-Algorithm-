def knapsack(price,wt,w):
    ratio = [price[i] / wt[i] for i in range(len(wt))]
    # Sort items by their value-to-weight ratio in descending order
    indices = sorted(range(len(ratio)), key=lambda i: ratio[i], reverse=True)
    profit = 0
    for i in indices:
        if wt[i]<= w:
            w -= wt[i]
            profit += price[i]
    return profit

wt = [10, 20, 30, 40, 50, 60]
price = [100, 250, 300, 210, 260, 350]
w = 100
print(knapsack(price,wt,w))