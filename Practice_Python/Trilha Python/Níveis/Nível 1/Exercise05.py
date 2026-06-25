"""
Conversão de moeda
Pergunte um valor em Reais (R$) e a cotação do Dólar. Converta e exiba em Dólares com 2 casas decimais.
"""

# Variables
money_real = float(input("Value money: "))
price_dollar = 5.50

# Printing values
print("R$ %.2f / U$%.2f = %.2f" %(money_real, price_dollar, (money_real * price_dollar)))