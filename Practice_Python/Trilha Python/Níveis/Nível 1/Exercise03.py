"""
Preço total
Pergunte o valor de um produto e a quantidade comprada. Calcule e exiba o total a pagar.
"""

# Variables
price_product = float(input("Price of product: "))
amount_sales = int(input("Amount of products: "))

# Printing value price final
print(f"The final price of product is R$ {price_product * amount_sales}")
