
# VERIFICA SOMA RECURSIVO
def soma_x(data, left, right):
    if((right <= left) or (right > len(data))): return False

    if(data[left] + data[right] > x):
        return soma_x(data, left, right-1)
    
    if(data[left] + data[right] < x):
        return soma_x(data, left+1, right)
    
    if(data[left] + data[right] == x): 
        print("\nSoma nos indices:")
        print("Array [",left,"] = ", data[left])
        print("Array [",right,"] = ", data[right])
        return True

# ENCONTRA VALOR APROXIMADO DE X (PELA ESQUERDA) RECURSIVAMENTE
def right_index(data, x, idx, mid):
    # QUANDO NAO HOUVER MAIS ESPACOS PRA PROCURAR
    if(mid<1): return idx
    # RECURSAO BUSCANDO VALOR PROXIMO
    if(data[idx] > x): return right_index(data, x, int(idx-mid), int(mid/2))
    else: return right_index(data, x, int(idx+mid), int(mid/2))

# APROXIMACAO PARA O VALOR
def approx(data, x):
    # SE MAIOR VALOR DO ARRAY AINDA EH MENOR Q X PROCURADO
    if(max(data) < x): return data.index(max(data)) 
    # BUSCAR VALOR PROXIMO
    mid = len(data)/2
    idx_mid = (len(data)-1)/2
    return right_index(data, x, int(idx_mid), int(mid))

# DEFINICAO DO VETOR BASE
data = [1, 2, 3, 4, 6, 7, 8, 9, 10]
n = len(data)

# LEITURA DO VALOR X
x = int(input("Valor de X: "))

if(x not in data):
    right = approx(data, x)
else:
    right = data.index(x)

left = 0

if(soma_x(data, left, right) == False):
    print("Soma nao foi encontrada.")


