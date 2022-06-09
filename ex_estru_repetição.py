print("exercício 01 estrutura de repetição\n")
s = 0
for x in range(3, 334, 3):
    s += x
print("soma = ", s)

print('\n\n')

print("\nExercicio 02 estrutura de repetição\n")
s = 0
for contador in range(1,11):
  nota = float(input("digite a nota "+str(contador)+": "))
  s += nota
print("media = ",s/10)

print('\n\n')

print("\nExercicio 03 estrutura de repetição\n")
numero = int(input("digite o numero para a tabuada: "))
for sequencia in range(1,11):
  print("%2d x %2d = %5d"%(sequencia,numero,sequencia*numero))
  #%2d -> serve para criar um alinhamneto de colunas entre os valores

