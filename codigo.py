faturamento = int(input("Qual o valor do futuramento ? "))
custo = int(input("Qual foi o custo? "))
imposto = faturamento * 0.1
novasVendas = str(input("Existe novas vendas? "))

if novasVendas in "Ss":
    valorNovaVendas = int(input("Qual é valor entrou? "))
    faturamento = faturamento + valorNovaVendas

lucro = faturamento - custo - imposto
margemDeLucro = lucro / faturamento 


print(f"Seu faturamento foi R${faturamento}")
print(f"O custo foi de R$ {custo}")
print(f"Seu lucro foi R$ {lucro} ")
print(f"A margem de lucro foi de {round(margemDeLucro,2)}")
