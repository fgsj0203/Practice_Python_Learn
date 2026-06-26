"""
Salário com comissão
Leia o salário fixo de um vendedor e o total de vendas. Calcule a comissão (5% das vendas) e exiba o salário final.
"""

# Variables
salary = float(input("Salary: "))
total_sales = float(input("Value total of sales: "))

# Operations Logical
comission_value = total_sales * 0.05
salary_final = salary + comission_value

# Printing
print("The salary is: %.2f" %(salary))
print("The comission is: %.2f" %(comission_value))
print("The salary with comission is: %.2f" %(salary_final))




