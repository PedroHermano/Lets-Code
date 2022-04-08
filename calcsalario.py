from tkinter import END


salbruto = float(input ('Qual o valor do salário? '))
irpf = float(input('Qual a taxa do IRPF? '))
inss = float(input('Qual a taxa do INSS? '))
sindicato = float(input('Qual a taxa da contribuição SINDICAL? '))

print('=-' *30)

print('Salário bruto é:', salbruto)
print('A taxa do IRPF é: ', irpf, '%')
print('A taxa do INSS é: ',inss, '%')
print('A taxa do Sindicato é: ',sindicato, '%')
 
print('=-' *30)

subttirpf = float()
subttirpf = (salbruto * irpf)/100

subttinss = float()
subttinss = (salbruto * inss)/100

subttsindicato = float()
subttsindicato = (salbruto * sindicato)/100

print('O desconto do IRPF é: ', subttirpf)
print('O desconto do INSS é: ', subttinss)
print('O desconto do Sindicato é: ', subttsindicato)

print('=-' *30)

salarioliq = float()
salarioliq = salbruto - (subttirpf + subttinss + subttsindicato)

print('O salário líquido é de: ', salarioliq)

END