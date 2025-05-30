# MERGE SORT

def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        esquerda = merge_sort(arr[:meio])
        direita = merge_sort(arr[meio:])
        
        return merge(esquerda, direita)
    return arr

def merge(esq, dir):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado

# Vantagens:
# Complexidade garantida de O(n log n)
# Estável

# Desvantagens:
# Requer memória extra
