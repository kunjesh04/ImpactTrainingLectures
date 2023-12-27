# Program to find EMI

basic_salary = int(input('Enter Your basic_salary : '))
tax = 0
price = int(input('Enter Price of Car : '))
tenure = int(input('Enter the Tenure /(5 or 7 years) : '))
roi = 7.5

HRA, TA, FA = 0.35*(basic_salary), 0.15*(basic_salary), 0.1*(basic_salary)
gross_salary =  HRA + TA + FA + basic_salary
PF = 0.08*(gross_salary)
insurance = 0.015*(gross_salary)
net_salary = gross_salary - PF - insurance 

if net_salary>0 and net_salary<=500000:
    tax = 0 
elif net_salary>500000 and net_salary<=750000:
    tax = 0 + ((net_salary-500000)*0.05)
elif net_salary>750000 and net_salary<=1000000:
    tax = 0 + 12500 + ((net_salary-750000)*0.1)
else:
    tax = 0 + 12500 + 25000 + ((net_salary - 1000000)*0.2)

P = net_salary
R = roi
T = tenure
Interest = P*T*R/100

Total_amt = P + Interest
Months = T*12
EMI = price/Months

print("Net Salary : ", net_salary)
print('-'*25)
if (EMI<=(net_salary/12)*0.1):
    print("Yes, it is Possible.")
    print('Monthly EMI : ', round(EMI, 2))
else:
    print('Not Possible.')
