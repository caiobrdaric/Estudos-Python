salario = float(input("Digite o valor de salário:"))
aliquota = 0
salLiq = 0
    
if (salario <= 1903.38):
    salLiq = salario

if (salario >= 1903.39 and salario <= 2826.65):
    aliquota=0.925
    salLiq=(salario*aliquota)-142.80

if (salario >= 2826.66 and salario <= 3751.06):
    aliquota=0.85
    salLiq=(salario*aliquota)-354.80;

if (salario >= 3751.07 and salario <= 4664.68):
    aliquota=0.775;
    salLiq=(salario*aliquota)-636.13;
 
if (salario >= 4664.69):
    aliquota=0.725
    salLiq=(salario*aliquota)-869.36

print ("Salário liquido de:", +salLiq)
