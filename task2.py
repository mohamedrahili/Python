# Q1: Create the Sales Data List and Review Data
weekly_sales = [3200, 4500, 0, 4100, 3700, 4200, 4600]
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("First element:", weekly_sales[0])  
print("Last element:", weekly_sales[-1])

# Q2: Calculate Total Sales
total_sales = sum(weekly_sales)
print("Total Sales:", total_sales)

# Q3: Update Data: Add New Sales Amount
weekly_sales.append(4500)
print("Updated weekly sales:", weekly_sales)

# Q4: Insert Missing Data
weekly_sales[2] = 3800  
print("After inserting Wednesday's sales:", weekly_sales)

# Q5: Delete Incorrect Data
weekly_sales.pop() 
print("After deleting incorrect data:", weekly_sales)

# Q6: Sort Data
sorted_sales = sorted(weekly_sales)  
print("Sorted sales data:", sorted_sales)

# Q7: Find the Highest and Lowest Sales
highest_sales = max(weekly_sales)
lowest_sales = min(weekly_sales)
print("Highest sales:", highest_sales)
print("Lowest sales:", lowest_sales)

# Q8: Extract the First Five Days of Sales Data
first_five_days = week[:5]
print("First five days of sales:", first_five_days)

# Q9: Print each day's Sales Value
for i in range(len(week)):
    print(f"The Sales Value on {week[i]} is {weekly_sales[i]}")