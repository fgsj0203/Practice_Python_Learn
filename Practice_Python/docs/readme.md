# Praticando a linguagem Python baseado em níveis

🟢 NÍVEL 1 - MUITO FÁCIL (Aquecimento - 5 exercícios)
Cumprimento personalizado
Crie um programa que pergunta o nome do usuário e exibe: "Olá, [nome]! Bem-vindo ao Python."

Idade em meses
Peça a idade do usuário em anos e converta para meses. Exiba: "Você tem [meses] meses de vida."

Preço total
Pergunte o valor de um produto e a quantidade comprada. Calcule e exiba o total a pagar.

Antecessor e sucessor
Leia um número inteiro e mostre seu antecessor e sucessor no formato: "Antecessor: X, Sucessor: Y"

Conversão de moeda
Pergunte um valor em Reais (R$) e a cotação do Dólar. Converta e exiba em Dólares com 2 casas decimais.

🟡 NÍVEL 2 - FÁCIL (Conceitos básicos - 8 exercícios)
Média aritmética
Leia 3 notas (valores decimais) e calcule a média aritmética. Exiba o resultado.

Área do círculo
Leia o raio de um círculo, calcule sua área (π * raio²) e exiba. Use π = 3.14159.

Conversão de temperaturas
Leia uma temperatura em Celsius e converta para Fahrenheit (F = C * 9/5 + 32).

Cálculo do troco
Pergunte o valor da compra e o valor pago. Calcule e exiba o troco.

Dias para horas
Leia um número de dias e converta para horas, minutos e segundos. Exiba os 3 valores.

Perímetro do retângulo
Leia a base e a altura de um retângulo. Calcule seu perímetro (2 * (base + altura)).

Desconto progressivo
Leia o valor de um produto e um percentual de desconto. Calcule o valor final com desconto.

Salário com comissão
Leia o salário fixo de um vendedor e o total de vendas. Calcule a comissão (5% das vendas) e exiba o salário final.

🟠 NÍVEL 3 - INTERMEDIÁRIO (Lógica e conversões - 8 exercícios)
Média ponderada
Leia 3 notas e seus respectivos pesos (ex: peso 2, 3, 5). Calcule a média ponderada e exiba.

Conversão de tempo
Leia uma quantidade de segundos e converta para horas, minutos e segundos. Ex: 3665 → 1h 1min 5s.

Cálculo de juros simples
Leia capital inicial, taxa de juros (%) e tempo (meses). Calcule o montante final (Juros = Capital * Taxa * Tempo / 100).

Distância entre dois pontos
Leia as coordenadas (x1, y1) e (x2, y2) de dois pontos. Calcule a distância euclidiana: √((x2-x1)² + (y2-y1)²).

Validação de CPF (parte 1)
Leia um número de CPF (apenas números, 11 dígitos). Armazene em uma variável e exiba no formato "XXX.XXX.XXX-XX".

Calculadora de IMC avançada
Além de calcular o IMC, exiba a classificação baseada na tabela da OMS (magreza, normal, sobrepeso, etc.). Use apenas if (sim, você já pode usar).

Custo de viagem
Leia distância (km), consumo do carro (km/l) e preço do combustível (R$/l). Calcule o custo total da viagem.

Conversão de unidades
Leia um valor em metros e converta para centímetros, milímetros e quilômetros. Exiba os 3 valores.

🔴 NÍVEL 4 - DESAFIADOR (Raciocínio e segurança - 5 exercícios)
Validação de senha simples
Leia uma senha e armazene em uma variável. Exiba o tamanho da senha e o primeiro e último caractere.

Manipulação de strings
Leia o nome completo de uma pessoa. Exiba:

Quantas letras tem (sem espaços)

O nome em maiúsculas

O nome em minúsculas

A primeira e a última letra

Gerador de hash (simulado)
Leia uma palavra e exiba o comprimento dela. Em seguida, exiba uma "hash" simulada: substitua cada letra pelo código ASCII dela (use ord()). Ex: "abc" → "97-98-99".

Cálculo de gorjeta
Leia o valor da conta de um restaurante e a porcentagem de gorjeta (ex: 10, 15, 20). Calcule o valor da gorjeta e o total a pagar. O resultado deve ter 2 casas decimais.

Extraindo dados de um IP
Leia um endereço IP no formato "192.168.1.1" (string). Separe os 4 octetos e exiba cada um em uma linha. Dica: use split().

⚫ NÍVEL 5 - DESAFIO EXTREMO (Para fixar TUDO - 4 exercícios)
Simulador de empréstimo
Leia o valor do empréstimo, a taxa de juros mensal (%) e o número de parcelas. Calcule o valor da parcela usando a fórmula de juros compostos:
Parcela = Valor * (Taxa * (1 + Taxa)^Parcelas) / ((1 + Taxa)^Parcelas - 1)
(Dica: use ** para potência)

Gerador de e-mails corporativos
Leia o primeiro nome e o sobrenome de um funcionário. Gere o e-mail no formato: "primeiro.sobrenome@empresa.com" (tudo minúsculo). Considere que pode haver espaços extras.

Manipulação de data (formato BR)
Leia uma data no formato "DD/MM/AAAA" (string). Extraia o dia, mês e ano e exiba no formato "AAAA-MM-DD". Use split() e concatenação.

Sistema de autenticação de dois fatores (simulado)
Leia o nome de usuário e uma senha numérica de 4 dígitos.

Exiba o nome invertido (ex: "João" → "oãoJ")

Exiba a senha com os dígitos ocultos (ex: "1234" → "****")

Calcule a soma dos dígitos da senha.

📋 COMO ORGANIZAR SEU ESTUDO HOJE
Etapa	O que fazer	Tempo
1	Leia rapidamente TODOS os 30 exercícios	10 min
2	Resolva do 1 ao 15 (Níveis 1 e 2)	30 min
3	Faça uma pausa de 5 min	-
4	Resolva do 16 ao 30 (Níveis 3, 4 e 5)	50 min
5	Revise os que você errou ou teve dúvida	20 min
6	Anote no seu anotacoes.txt:
- Quais tipos de erro cometeu
- Quais exercícios foram mais difíceis	10 min
🧠 DICAS PARA RESOLVER SEM RESPOSTAS
Use type() para verificar o tipo da variável se tiver dúvida.

Converta tudo para float quando for fazer contas com números decimais.

Lembre-se: input() sempre retorna string. Use int() ou float() para números.

Teste com valores extremos: -0, 999999, 0.0001, strings vazias.

Se travar em um exercício por mais de 10 min, PULE e volte depois. A mente processa em segundo plano.

✅ CRITÉRIOS DE SUCESSO PARA O DIA 1
Você sabe que dominou o conteúdo quando:

Consegue fazer os 30 exercícios em menos de 1h30

Não precisa consultar o Google para print(), input() ou conversões

Identifica imediatamente quando vai ter erro de tipo (TypeError)

Sabe a diferença entre 10/3 (float) e 10//3 (int)

Amanhã, no Dia 2, serão 30 exercícios sobre operadores aritméticos, comparação e lógicos. Você quer que eu já te envie a lista ou prefere receber no final do dia, depois que terminar estes?

Bons estudos! Se tiver dúvida em algum exercício específico (sem pedir a resposta), me pergunte que eu dou uma dica. 🚀

