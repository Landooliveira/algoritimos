numeros = []

while True:
    n = int(input("Digite um numero 0 para encerrar : "))
    
    if n == 0:
        break
        
    numeros.append(n)

soma = sum(numeros)
print("numeros digitados:", numeros)
print ("soma dos valores:",soma)

