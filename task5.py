def get_sales_data():  
    return [100, 200, 150, 300, 250]

def analyze_sales(sales):   
    total_sales = sum(sales)
    average_sales = total_sales / len(sales)
    max_sales = max(sales)
    min_sales = min(sales)
    return total_sales, average_sales, max_sales, min_sales

sales = get_sales_data()

total_sales, average_sales, max_sales, min_sales = analyze_sales(sales)

print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales}")
print(f"Max Sales: {max_sales}")
print(f"Min Sales: {min_sales}")

def target_check(total_sales, target):
    if total_sales >= target:
        print("Target achieved")
    else:
        print("Target not achieved")
target = 2000  

target_check(total_sales, target)
