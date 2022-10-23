for i in range (30):
    if (i % 2==0):{
    print (i)
}
n = 0
while (n <= 30):
    if (n % 2==0):{
        print (n)
    }
    n += 1   
for i in range (30):
    if (i % 2==1):{
    print (i)
}
n = 0
while (n <= 30):
    if (n % 2==1):{
        print (n)
    }
    n += 1   
Name= "Ahmed"
Total_Amount= float(50000)
Marketing =(0.25 * float(Total_Amount))
Operational_Expenses = (0.5* float(Total_Amount))
Total_customer_Aquisition = (0.25* float(Total_Amount))
Financial_statement = (f"Hello {Name}!\n your financial statement is as follows:\n Marketing Expenses = {Marketing}\n Operational Expenses = {Operational_Expenses}\n Customer Aquisition = {Total_customer_Aquisition}\n Total amount allocated = {Total_Amount}" )
print (Financial_statement)

Max_possible_customer= (Total_customer_Aquisition/5)
print(f"The total number of customers you can acquire with the budget is {Max_possible_customer}")


