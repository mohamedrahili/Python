weekly_sales = [2000, 3000, 4000, 5000, 6000, 2500, 3500]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
target = 20000
cumulative_sales = 0

for day_name, sales in zip(days_of_week, weekly_sales):
    if sales > 5000:
        print(f"{day_name}: High Sales Day Alert")
    else:
        print(f"For {day_name} sales are normal")
        while sales < 5000:
            sales += 500
    
    cumulative_sales += sales
    
    if cumulative_sales > target:
        print("Target Reached!")
        break
else:
    print("Target Not Reached.")
