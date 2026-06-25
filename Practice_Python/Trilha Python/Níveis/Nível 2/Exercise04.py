"""
Cálculo do troco
Pergunte o valor da compra e o valor pago. Calcule e exiba o troco.
"""

# Variables
value_sale = float(input("The value of sale: "))
value_payment = float(input("The value of payment: "))

# Printing
print(f"The exchange of {value_sale} and value_payment {value_payment} is {(value_sale - value_payment) * -1}")