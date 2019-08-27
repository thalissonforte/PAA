
# DEFINICAO DO VETOR BASE
data = [3, 1, 2, 6, 4, 10, 9, 5, 0]
#data = [2, 3, 8, 6, 1]
n = len(data)
inversoes = 0
left = 0

while(left < n-1):
    if(data[left] > data[left+1]):
        inversoes += 1
        print("[", data[left] ,", ", data[left+1] ,"]")
    
    left += 1

print("Total inversoes: ", inversoes)
