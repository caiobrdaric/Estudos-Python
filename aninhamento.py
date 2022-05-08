categoria = int(input("Selecione a categoria:"))
if categoria == 1:
    preço = 25
elif categoria == 2: 
    preço = 50
elif categoria == 3:
    preço = 75
elif categoria == 4:
    preço = 100
elif categoria == 5:
    preço = 150
else:
    print("Categoria inválida, digite um numero de 1 a 5")
    preço = 0
print (f"O valor do serviço é R$ {preço:3.2f}")
