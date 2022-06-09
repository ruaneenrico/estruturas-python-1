print("exemplo 01 de while - enquanto\n")
senha = "54321"
leitura = " "
while (leitura != senha):
  leitura = input("digite a senha: ")
  if leitura == senha:
     print ('acesso liberado')
  else:
    print ('senha incorreta. tente novamente')

print('n\n')

print("\nExemplo 02 de While - Enquanto\n")
contador = 0
somador = 0
while contador < 5:
  contador = contador + 1
  valor = float(input('Digite o '+str(contador)+'º valor: '))
  somador = somador + valor
print('Soma = ',somador)
#str -> retornar a variável contador na forma de string

print('\n\n')

print("\nExemplo 01 de 'for'. encontrar a soma S = 1+4+7+10+13+16+19\n")
S = 0
for X in range(1,20,3):
  S += X
print('soma = ',S)
#a função range() define um intervalo de valores inteiros

print('\n\n')

print("\nExemplo 02 de 'for'. as notas de um aluno estao armazenadas em uma lista.calcuar a media dssas notas. ")
lista_notas = [3.4,6.6,8,9,10,9.5,8.8,4.3]
soma = 0
for nota in lista_notas:
  soma += nota
media = soma/len(lista_notas)
print('media = %.2f'%media)