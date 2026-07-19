sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales_w2.append(int(input('new day')))
sales = sales_w1 + sales_w2
best_sales = max(sales) * 1.5
worst_sales = min(sales) * 1.5
combined_sales = best_sales + worst_sales
print(f""" best sales = {best_sales} 
           worst sales = {worst_sales} 
           combined slaes = {combined_sales}""")
