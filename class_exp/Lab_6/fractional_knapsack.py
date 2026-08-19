def knapsack(price, wt, W):
    n = len(price)
    
    ratio = [] 

    for i in range(n):
        r = price[i] / wt[i]
        ratio.append((r, price[i], wt[i], i))
        
    ratio.sort(key=lambda x: x[0], reverse=True)

    profit = 0
    item = []
    
    for r, p, w, id in ratio:
        if w <= W:
            W -= w
            profit += p
            item.append(id)
        else :
            fraction = W / w
            profit += p * fraction
            W = 0
            item.append(id)
    return profit, item

wt = [10, 20, 30, 40, 50, 60]
price = [100, 250, 300, 210, 260, 350]
w = 100
print(knapsack(price, wt, w))
