"""
Desconto progressivo
Leia o valor de um produto e um percentual de desconto. Calcule o valor final com desconto.
"""

# Variables
value_product = float(input("Value of product: "))
percentual_discount = int(input("Value of discount: "))

# Printing
print(f"The value final {value_product - (value_product * (percentual_discount / 100))}")



