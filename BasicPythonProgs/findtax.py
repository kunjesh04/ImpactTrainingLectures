# Tax

basic_salary = int(input('Enter Your basic_salary : '))
tax = 0

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

print("Gross Salary : ", gross_salary)
print("Insurance : ", insurance)
print("PF : ", PF)

print('-'*25)

print("Net Salary : ", net_salary)
print("Tax : ", tax)