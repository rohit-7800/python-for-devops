#Task Calculate the Profit Percentage
cost_price =float(input("Enter the cost pricr of the item :"))
selling_price= float(input("Enter the selling price of the item :"))

if selling_price  > cost_price:
    profit = selling_price -cost_price
    profit_percentage =(profit / cost_price) * 100
    print(f"The profit percentage is: {profit_percentage:.2f}%")
elif selling_price < cost_price:
    loss = cost_price -selling_price
    loss_percentage = (loss / cost_price) * 100
    print(f"The loss percentage is: {loss_percentage:.2f}%")
else:
    print("No profit, no loss.")    