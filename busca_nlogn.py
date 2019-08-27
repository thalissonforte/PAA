
# VERIFICA SOMA RECURSIVO
def soma_x(data, left, right):
    if((right <= left) or (right > len(data))): return False

    if(data[left] + data[right] > x):
        soma_x(data, left, right-1)
    
    if(data[left] + data[right] < x):
        soma_x(data, left+1, right)
    
    if(data[left] + data[right] == x): 
        print("Soma nos indices: [",left,", ",right,"]")
        return True

# DEFINICAO DO VETOR BASE
data = [1, 2, 3, 4, 6, 7, 8, 9, 10]
n = len(data)

# LEITURA DO VALOR X
x = int(input("Valor de X: "))

if(x not in data):
    right = len(data)-1
else:
    right = data.index(x)

left = 0

if(soma_x(data, left, right) == False):
    print("Soma nao foi encontrada.")


